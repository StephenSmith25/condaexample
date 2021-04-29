cmake_minimum_required(VERSION 3.16)

project(condatest)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")

find_package(Nexus REQUIRED)

set(MINIMUM_PYTHON_VERSION 3.8)
set(Boost_USE_STATIC_LIBS OFF)
find_package(Python ${MINIMUM_PYTHON_VERSION} REQUIRED
             COMPONENTS Interpreter Development NumPy)
# If anything external uses find_package(PythonInterp) then make sure it finds
# the correct version and executable
set(PYTHON_EXECUTABLE ${Python_EXECUTABLE})
find_package(
  Boost REQUIRED
  COMPONENTS date_time regex serialization filesystem system
             python${Python_VERSION_MAJOR}${Python_VERSION_MINOR})

add_subdirectory(src)

