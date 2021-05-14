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

if(APPLE)
  set(MACOSX_BUNDLE_ICON_FILE "icon.icns")
  set(MACOSX_BUNDLE_GUI_IDENTIFIER "HelloWorld")
  set(MACOSX_BUNDLE_LONG_VERSION_STRING "1.0.0")
  set(MACOSX_BUNDLE_BUNDLE_NAME "HelloWorld")
  set(MACOSX_BUNDLE_SHORT_VERSION_STRING "1.0")
  set(MACOSX_BUNDLE_BUNDLE_VERSION "1.0.0")
  set(MACOSX_BUNDLE_COPYRIGHT "Stephen Smith")
endif(APPLE)

add_subdirectory(src)

include(GNUInstallDirs)
# if(NOT APPLE)
#   set(CMAKE_INSTALL_RPATH $ORIGIN)
# else()
#   set(CMAKE_INSTALL_RPATH @loader_path)
# endif()

if(BUILD_ALL OR QT_TEST)
    install(TARGETS helloworld 
            BUNDLE DESTINATION ${CMAKE_INSTALL_BINDIR} 
            RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}) 
endif()






# if(APPLE)
# if(BUILD_ALL OR QT_TEST)
#   set(CPACK_GENERATOR DragNDrop)
#   set(CPACK_BUNDLE_NAME QtExample)
#   set(CPACK_BUNDLE_ICON ${CMAKE_SOURCE_DIR}/packaging/osx_logo.png)
# endif()
# endif()


# option(ENABLE_CPACK "Switch to enable CPack package generation"  OFF)
# if(ENABLE_CPACK)
#   include(CPack)
# endif()


