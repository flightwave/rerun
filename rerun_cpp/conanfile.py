from conan import ConanFile
from conan.tools.files import get, copy, mkdir, download
from conan.tools.cmake import cmake_layout, CMakeToolchain, CMakeDeps, CMake
from conan.errors import ConanException

import os, glob
import re
import shutil

def _normalized_export_paths(patterns):
    # Strip trailing globs like *, *.cpp, **/*.h etc
    cleaned = set()
    for pattern in patterns:
        cleaned.add(re.split(r'[*?\[]', pattern)[0].rstrip("/\\"))
    return cleaned


class RerunCppSdkConan(ConanFile):
    name            = "rerun_cpp_sdk"
    license         = "Apache-2.0"
    url             = "https://github.com/rerun-io/rerun"
    description     = "Rerun C++ SDK with embedded Rust C core"
    settings        = "os", "arch", "compiler", "build_type"
    options         = {
        "shared": [True, False],
        "fPIC": [True, False],
    }
    default_options = {
        "shared": True,
        "fPIC": True,
    }
    requires        = ["arrow/20.0.0"]
    exports_sources = "src/*", "CMakeLists.txt"
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
        # This approach moves the sources coming from this recipes' folder to a
        # backup path (inside conan's cache) and then overwrite what we are downloading.
        # This is done this way since we need the lib/ files from the upstream sources

        renamed = []
        paths = _normalized_export_paths(self.exports_sources)

        for path in paths:
            abs_path = os.path.join(self.source_folder, path)
            backup_path = abs_path + "__backup__"
            if os.path.exists(abs_path):
                shutil.move(abs_path, backup_path)
                renamed.append((backup_path, abs_path))
                self.output.info(f"Renamed: {path} -> {os.path.basename(backup_path)}")


        # 2. Download SDK
        sdk_url = "https://github.com/rerun-io/rerun/releases/latest/download/rerun_cpp_sdk.zip"
        get(self, sdk_url, strip_root=True)

        # 3. Restore backups over SDK contents
        for backup, target in renamed:
            if os.path.exists(target):
                if os.path.isdir(target):
                    shutil.rmtree(target)
                else:
                    os.remove(target)
            shutil.move(backup, target)
            self.output.info(f"Restored: {target}")


    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["RERUN_DOWNLOAD_AND_BUILD_ARROW"] = False
        tc.cache_variables["RERUN_ARROW_LINK_SHARED"]       = False
        tc.cache_variables["RERUN_INSTALL_RERUN_C"]         = True
        tc.cache_variables["RERUN_C_LIB"] = os.path.join(
            self.source_folder, "lib", self._c_lib_filename()
        )
        tc.generate()

        deps = CMakeDeps(self)
        deps.generate()

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
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        # 1) CMake install
        cmake = CMake(self)
        cmake.install()

        # 2) Copy & rename the shipped C-core into a standard name
        libdir = os.path.join(self.package_folder, "lib")
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
        self.cpp_info.components["rerun_sdk"].requires = ["c_core", "arrow::arrow"]

        # Make sure `find_package(rerun_sdk)` works
        self.cpp_info.set_property("cmake_file_name",   "rerun_sdk")
        self.cpp_info.set_property("cmake_target_name", "rerun_sdk")
