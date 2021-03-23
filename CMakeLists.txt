cmake_minimum_required(VERSION 3.16)

project(condatest)

set(CMAKE_CXX_STANDARD 17)

find_package(Boost REQUIRED)

add_subdirectory(src)