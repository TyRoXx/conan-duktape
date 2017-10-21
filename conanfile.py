from conans import ConanFile
from conans.tools import download, unzip, replace_in_file, check_sha256
import os
import shutil
from conans import CMake, ConfigureEnvironment

class DuktapeConan(ConanFile):
    name = "duktape"
    version = "1.5.0"
    settings = "os", "arch", "compiler", "build_type"
    exports = "CMakeLists.txt"
    generators = "cmake"
    url = "http://github.com/TyRoXx/conan-duktape"
    license = "MIT"
    source_root = "duktape-1.5.0"

    def source(self):
        zip_name = "duktape-1.5.0.tar.xz"
        download("http://duktape.org/%s" % zip_name, zip_name)
        check_sha256(zip_name, "7ed8838eb33b8a11433241c990bf9aa9803b7f4a1618eaf8fdb4c3a884e93ec0")
        self.run("cmake -E tar xf %s" % zip_name)
        shutil.move("CMakeLists.txt", "%s/CMakeLists.txt" % self.source_root)

    def build(self):
        self.run("mkdir _build")
        cmake = CMake(self)
        cmake.configure(source_dir=self.conanfile_directory, build_dir="./_build")
        cmake.build()

    def package(self):
        self.copy(pattern="*.h", dst="include", src="%s/src" % self.source_root, keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="_build", keep_path=False)
        self.copy(pattern="*.a", dst="lib", src="_build", keep_path=False)

    def package_info(self):  
        self.cpp_info.libs = ["duktape"]
