#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile, tools, CMake


class LibSedMLConan(ConanFile):

    name = "libsedml"
    version = "2.0.11"
    url = "http://github.com/fbergmann/conan-libsedml"
    homepage = "https://github.com/fbergmann/libSEDML/"
    author = "Frank Bergmann"
    license = "BSD"

    description = ("This project makes use of libSBML XML layer as well as code generation as starting point to produce a library for reading and writing of SED-ML models.")

    settings = "os", "arch", "compiler", "build_type"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "cpp_namespaces": [True, False]
    }

    default_options = (
        "shared=False",
        "fPIC=True",
        "cpp_namespaces=False"
    )

    generators = "cmake", "cmake_paths"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

        self.requires("libsbml/5.18.3@fbergmann/stable")
        self.options['libsbml'].shared = self.options.shared
        self.requires("libnuml/1.1.1@fbergmann/stable")
        self.options['libnuml'].shared = self.options.shared

    def source(self):
        git = tools.Git("src")
        git.clone("https://github.com/fbergmann/libSEDML/", branch="level1-version4")

    def _configure(self, cmake):
        args = ['-DEXTRA_LIBS=expat;bz2;zlib']
        if self.options.cpp_namespaces:
            args.append('-DWITH_CPP_NAMESPACE=ON')
        if self.settings.compiler == 'Visual Studio' and 'MT' in self.settings.compiler.runtime:
            args.append('-DWITH_STATIC_RUNTIME=ON')
        if not self.options.shared:
            args.append('-DLIBSEDML_SKIP_SHARED_LIBRARY=ON')
            args.append('-DLIBSEDML_SHARED_VERSION=OFF')

        cmake.configure(build_folder="build", args=args, source_folder="src")

    def build(self):
        cmake = CMake(self)
        self._configure(cmake)
        cmake.build()
        cmake.test()

    def package(self):
        cmake = CMake(self)
        self._configure(cmake)
        cmake.install()
        cmake.patch_config_paths()
        self.copy("*.lib", dst="lib", keep_path=False)
        if self.settings.os == "Windows":
            self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):

        libfile = "libsedml"

        if not self.settings.os == "Windows":
            if self.options.shared:
                if self.settings.os == "Linux":
                    libfile += ".so"
                if self.settings.os == "Macos":
                    libfile += ".dylib"
            else:
                libfile += "-static.a"
        else:
            if self.options.shared:
                libfile += ".dll"
            else:
                libfile += "-static.lib"

        self.cpp_info.libs = [libfile]

        if not self.options.shared:
            self.cpp_info.defines = ["LIBSEDML_STATIC"]
