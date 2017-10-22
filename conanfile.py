from conans import ConanFile
from conans.tools import download, unzip, replace_in_file, check_sha256
import os
import shutil
from conans import CMake, ConfigureEnvironment

class DuktapeConan(ConanFile):
    name = "duktape"
    version = "2.2.0"
    settings = "os", "arch", "compiler", "build_type"
    exports = "CMakeLists.txt"
    generators = "cmake"
    url = "http://github.com/TyRoXx/conan-duktape"
    license = "MIT"
    source_root = "duktape-2.2.0"

    def source(self):
        zip_name = "duktape-2.2.0.tar.xz"
        download("http://duktape.org/%s" % zip_name, zip_name)
        check_sha256(zip_name, "62f72206427633077cb02e7ccd2599ace4d254db409334593b86d262c0d50c14")
        self.run("cmake -E tar xf %s" % zip_name)
        shutil.move("CMakeLists.txt", "%s/CMakeLists.txt" % self.source_root)

    def build(self):
        self.run("mkdir _build")
        cmake = CMake(self)
        cmake.configure(source_dir=("%s/%s" % (self.conanfile_directory, self.source_root)), build_dir="./_build")
        cmake.build(build_dir="./_build")

    def package(self):
        self.copy(pattern="*.h", dst="include", src="%s/src" % self.source_root, keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src="_build", keep_path=False)
        self.copy(pattern="*.a", dst="lib", src="_build", keep_path=False)

    def package_info(self):  
        self.cpp_info.libs = ["duktape"]
