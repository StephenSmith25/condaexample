cmake_minimum_required(VERSION 3.16)

project(condatest)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/CMake")

find_package(Boost REQUIRED)
find_package(Nexus REQUIRED)

add_subdirectory(src)

