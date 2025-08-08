from conan import ConanFile
from conan.tools.files import get, copy
from conan.tools.cmake import cmake_layout, CMakeToolchain, CMakeDeps, CMake
from conan.tools.env import Environment
from conan.errors import ConanException
import os, glob
import re

class RerunCppSdkConan(ConanFile):
    name            = "rerun_cpp_sdk"
    license         = "Apache-2.0"
    url             = "https://github.com/rerun-io/rerun"
    description     = "Rerun C++ SDK with embedded Rust C core"
    settings        = "os", "arch", "compiler", "build_type"
    options         = {"shared": [True, False]}
    default_options = {"shared": False}
    requires        = ["arrow/15.0.0", "loguru/cci.20230406"]
    exports_sources = "lib/*", "lib_arm/*", "src/*", "CMakeLists.txt"
    no_copy_source  = False

    def layout(self):
        cmake_layout(self)

    def set_version(self):
        # Read version from sdk_info.h
        sdk_info_path = os.path.join(self.recipe_folder, "src", "rerun", "c", "sdk_info.h")
        if os.path.exists(sdk_info_path):
            with open(sdk_info_path, "r") as f:
                content = f.read()
                version_match = re.search(r'#define\s+RERUN_SDK_HEADER_VERSION\s+"([^"]+)"', content)
                if version_match:
                    self.version = version_match.group(1)
                else:
                    raise ConanException("Could not find RERUN_SDK_HEADER_VERSION in sdk_info.h")
        else:
            raise ConanException("Could not find sdk_info.h at path: " + sdk_info_path)

    def source(self):
        # Always download the SDK first, then we'll add source files in build() if needed
        sdk_url = (
            f"https://github.com/rerun-io/rerun/releases/latest/download/rerun_cpp_sdk.zip"
        )
        get(self, sdk_url, strip_root=True)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["RERUN_DOWNLOAD_AND_BUILD_ARROW"] = False
        tc.cache_variables["RERUN_ARROW_LINK_SHARED"]       = False
        tc.cache_variables["RERUN_INSTALL_RERUN_C"]         = True

        # For ARM architectures, build rerun_c from source instead of using pre-compiled binary
        if self._needs_source_build():
            # Point to the library we'll build from source
            tc.cache_variables["RERUN_C_LIB"] = os.path.join(
                self.source_folder, "lib", "librerun_c.a"
            )
        else:
            tc.cache_variables["RERUN_C_LIB"] = os.path.join(
                self.source_folder, "lib", self._c_lib_filename()
            )
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

    def _needs_source_build(self):
        """Check if we need to build rerun_c from source instead of using pre-compiled binary"""
        arch = str(self.settings.arch)
        # For ARM32 (armv7hf), we need to build from source as no pre-compiled binary exists
        return arch in ["armv7hf", "armv7"]

    def _c_lib_filename(self):
        mapping = {
            "Linux":  {"x86_64": "librerun_c__linux_x64.a",  "armv8": "librerun_c__linux_arm64.a"},
            "Macos":  {"x86_64": "librerun_c__macos_x64.a",  "armv8": "librerun_c__macos_arm64.a"},
            "Windows":{"x86_64": "rerun_c__win_x64.lib"},
        }
        os_  = str(self.settings.os)
        arch = str(self.settings.arch)
        try:
            return mapping[os_][arch]
        except KeyError:
            raise ConanException(f"No rerun_c binary for {os_}/{arch}")

    def build(self):
        if self._needs_source_build():
            # Use pre-built ARM library
            self._use_prebuilt_arm_library()

        # Build the C++ SDK
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def _use_prebuilt_arm_library(self):
        """Use the pre-built ARM rerun_c library"""
        # Copy the pre-built ARM library to the expected location
        lib_dir = os.path.join(self.source_folder, "lib")
        os.makedirs(lib_dir, exist_ok=True)
        copy(self, "librerun_c.a",
             src=os.path.join(self.source_folder, "lib_arm"),
             dst=lib_dir)

    def package(self):
        # 1) CMake install
        cmake = CMake(self)
        cmake.install()

        # 2) Handle C library packaging
        libdir = os.path.join(self.package_folder, "lib")

        if self._needs_source_build():
            # For source builds, the library should already be built and installed by CMake
            # Just ensure the standard name exists
            if self.settings.os == "Windows":
                expected_name = "rerun_c.lib"
            else:
                expected_name = "librerun_c.a"

            # Check if the library exists in the expected location
            expected_path = os.path.join(libdir, expected_name)
            if not os.path.exists(expected_path):
                self.output.warn(f"Expected rerun_c library not found at {expected_path}")
        else:
            # For pre-compiled binaries, copy & rename the shipped C-core
            c_filename = self._c_lib_filename()
            # copy the exactly-matching file:
            copy(self, c_filename,
                 src=os.path.join(self.source_folder, "lib"),
                 dst=libdir,
                 keep_path=False)

            # now rename it to the standard name
            if self.settings.os == "Windows":
                new_name = "rerun_c.lib"
            else:
                new_name = "librerun_c.a"
            old_path = os.path.join(libdir, c_filename)
            new_path = os.path.join(libdir, new_name)
            os.replace(old_path, new_path)

        # 3) Copy headers into include/
        copy(self, "*.hpp",
             src=os.path.join(self.source_folder, "src"),
             dst=os.path.join(self.package_folder, "include"))
        copy(self, "*.h",
             src=os.path.join(self.source_folder, "src"),
             dst=os.path.join(self.package_folder, "include"))

    def package_info(self):
        # C-core component
        self.cpp_info.components["c_core"].libs = ["rerun_c"]
        # C++ SDK component
        self.cpp_info.components["rerun_sdk"].libs     = ["rerun_sdk"]
        self.cpp_info.components["rerun_sdk"].requires = ["c_core", "arrow::arrow", "loguru::loguru"]

        # Make sure `find_package(rerun_sdk)` works
        self.cpp_info.set_property("cmake_file_name",   "rerun_sdk")
        self.cpp_info.set_property("cmake_target_name", "rerun_sdk")
