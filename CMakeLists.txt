cmake_minimum_required(VERSION 3.16)

project(condatest)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake")



option(BUILD_ALL "Build all tests" ON ) 
option(BOOST_TEST "Builds boost project test" OFF)
option(COMPILER_TEST "Builds compiler test" OFF)
option(STDLIB_TEST "Builds stdlib test" OFF)
option(ALL_LIB_TEST "Builds all_cpp_lib_check_test" OFF)
option(NEXUS_TEST "Builds the nexus test" OFF)
option(PYQT_TEST "Builds the pyqt test" OFF)
option(QT_TEST "Builds the qt example" OFF)


if (BUILD_ALL OR NEXUS_TEST OR ALL_LIB_TEST)
find_package(Nexus REQUIRED)
endif()

if (BUILD_ALL OR ALL_LIB_TEST OR BOOST_TEST OR PYQT_TEST)
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
endif()

add_subdirectory(src)

include(GNUInstallDirs)
if(NOT APPLE)
  set(CMAKE_INSTALL_RPATH $ORIGIN)
else()
  set(CMAKE_INSTALL_RPATH @loader_path)
endif()

if(BUILD_ALL OR QT_TEST)
    install(TARGETS helloworld 
            ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
            LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
            RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}) 

endif()

