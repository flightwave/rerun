import os
import tarfile
from conan import ConanFile
from conan.tools.files import download, mkdir, copy

class L4TToolchain(ConanFile):
    name = "l4t-toolchain"
    version = "1.0"
    package_type = "application"
    settings = "os", "arch"

    def build(self):
        url = "https://developer.nvidia.com/embedded/jetson-linux/bootlin-toolchain-gcc-93"
        archive_name = "bootlin-toolchain-gcc-93"
        archive_path = os.path.join(self.build_folder, archive_name)
        toolchain_dir = os.path.join(self.build_folder, "toolchain")

        if not os.path.exists(toolchain_dir):
            mkdir(self, toolchain_dir)
            self.output.info(f"Downloading toolchain from {url}")
            download(self, url, archive_path)

            self.output.info(f"Extracting to {toolchain_dir}")
            with tarfile.open(archive_path) as tf:
                tf.extractall(path=toolchain_dir)

    def package(self):
        toolchain_src = os.path.join(self.build_folder, "toolchain")
        copy(self, "*", src=toolchain_src, dst=self.package_folder, keep_path=True)

    def package_info(self):
        bin_dir = os.path.join(self.package_folder, "bin")

        cc = os.path.join(bin_dir, "aarch64-buildroot-linux-gnu-cc")
        cxx = os.path.join(bin_dir, "aarch64-buildroot-linux-gnu-g++")
        ld = os.path.join(bin_dir, "aarch64-buildroot-linux-gnu-ld")

        self.env_info.PATH.append(bin_dir)

        self.conf_info.define("tools.build:compiler_executables", {
            "c": cc,
            "cpp": cxx,
            "ld": ld
        })

    def generate(self):
        bin_dir = os.path.join(self.package_folder, "bin")

        cc = os.path.join(bin_dir, "aarch64-buildroot-linux-gnu-cc")
        cxx = os.path.join(bin_dir, "aarch64-buildroot-linux-gnu-g++")
        ld = os.path.join(bin_dir, "aarch64-buildroot-linux-gnu-ld")

        self.buildenv_info.define("CC", cc)
        self.buildenv_info.define("CXX", cxx)
        self.buildenv_info.define("LD", ld)
        self.buildenv_info.append_path("PATH", bin_dir)
