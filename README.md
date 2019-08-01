
## Conan package recipe for [*libSEDML*](http://sed-ml.org/)



## Issues
All conan specific issues should be tracked in this projects 

To report possible libSEDML bugs or other issues:

* [libSEDML issue tracker](https://github.com/fbergmann/libsedml/issues)

## For Users

### Basic setup

    $ conan install libsedml/0.4.5@fbergmann/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    libsedml/0.4.5@fbergmann/stable

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . conan/stable


### Available Options

| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| shared      | False |  [True, False] |
| fPIC      | True |  [True, False] |
|cpp_namespaces| False| [True, False] | 
              
## Add Remote

You might need to add the Conan Center repo before installing the package:

    $ conan remote add conan-center "https://conan.bintray.com"


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package zlib.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](LICENSE)
