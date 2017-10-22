PROJECT(duktapetest)
cmake_minimum_required(VERSION 2.8)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
CONAN_BASIC_SETUP()

ADD_EXECUTABLE(duktapetest duktapetest.c)
include_directories(${CONAN_INCLUDE_DIRS})
target_link_libraries(duktapetest ${CONAN_LIBS})
if(NOT MSVC)
    target_link_libraries(duktapetest m)
endif()
