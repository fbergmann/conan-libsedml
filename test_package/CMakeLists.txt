PROJECT(LibSedMLPackageTest)
cmake_minimum_required(VERSION 2.8.12)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

ADD_EXECUTABLE(create_sedml create_sedml.cpp)
TARGET_LINK_LIBRARIES(create_sedml ${CONAN_LIBS})
