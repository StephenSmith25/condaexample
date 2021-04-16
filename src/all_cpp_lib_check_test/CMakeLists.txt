find_package(TBB REQUIRED)

set(MINIMUM_PYTHON_VERSION 3.8)
find_package(PythonLibs 3.8 REQUIRED)
find_package(Python ${MINIMUM_PYTHON_VERSION} REQUIRED
             COMPONENTS Interpreter Development NumPy)
# If anything external uses find_package(PythonInterp) then make sure it finds
# the correct version and executable
set(PYTHON_EXECUTABLE ${Python_EXECUTABLE})
set(Python_ADDITIONAL_VERSIONS ${Python_VERSION_MAJOR}.${Python_VERSION_MINOR})

# Handle switching between previously configured Python verions
if(Python_INCLUDE_DIR
   AND NOT Python_INCLUDE_DIR MATCHES
       ".*${Python_VERSION_MAJOR}\.${Python_VERSION_MINOR}.*")
  message(
    STATUS "Python version has changed. Clearing previous Python configuration."
  )
  unset_cached_python_variables()
endif()

find_package(
  Boost REQUIRED
  COMPONENTS date_time regex serialization filesystem system
             python${Python_VERSION_MAJOR}${Python_VERSION_MINOR})

find_package(Poco 1.10.1 REQUIRED)

find_package(Nexus REQUIRED)
# find_package(hdf REQUIRED) # Hdf4

# HDF5
if(CMAKE_HOST_WIN32)
  find_package(ZLIB REQUIRED CONFIGS zlib-config.cmake)
  set(HDF5_DIR "${MINICONDA_DIR}/cmake/hdf5")
  find_package(
    HDF5
    COMPONENTS CXX HL
    REQUIRED CONFIGS hdf5-config.cmake)
  set(HDF5_LIBRARIES hdf5::hdf5_cpp-shared hdf5::hdf5_hl-shared)
else()
  find_package(ZLIB REQUIRED)
  find_package(
    HDF5
    COMPONENTS CXX HL
    REQUIRED)
endif()

find_package(JemallocLib REQUIRED)

find_package(GSL REQUIRED)

find_package(JsonCPP REQUIRED)

find_package(LibRDKafka REQUIRED)

find_package(
  Qt5
  COMPONENTS Core
             Gui
             Widgets
             OpenGL
             Test
             Help
             Concurrent
             Xml
             WebKitWidgets
             Network
             PrintSupport
  REQUIRED)
find_package(QScintillaQt5 REQUIRED)
find_package(PyQt5 REQUIRED)
find_package(SIP REQUIRED)

find_package(Doxygen REQUIRED)

find_package(OpenMP COMPONENTS CXX)

# find_package(CxxTest REQUIRED)

find_package(OpenSSL REQUIRED)

find_package(Cppcheck REQUIRED) # Won't be needed in the future but maybe for
                                # initial Conda env?

if(MSVC)
  find_package(Lib3mf)
endif()

find_package(OpenCascade REQUIRED)

find_package(Eigen3 3.2 REQUIRED)

if(MSVC)
  find_package(Git 1.9.5 REQUIRED)
  find_package(GitLFS REQUIRED)
  find_package(Threads)
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
  find_package(Git REQUIRED)
endif()

if(NOT MSVC)
  add_compile_options(-ljemalloc)
endif()

add_executable(all_cpp_lib_check_test main.cpp)
target_link_libraries(
  all_cpp_lib_check_test
  ${Boost_LIBRARIES}
  ${PYTHON_LIBRARIES}
  TBB::tbb
  ${POCO_LIBRARIES}
  ${NEXUS_LIBRARIES}
  ${HDF5_LIBRARIES}
  ${GSL_LIBRARIES}
  ${JSONCPP_LIBRARIES}
  ${LibRDKafka_LIBRARIES}
  Qt5::Core
  Qt5::Gui
  Qt5::Widgets
  Qt5::OpenGL
  Qt5::Test
  Qt5::Help
  Qt5::Concurrent
  Qt5::Xml
  Qt5::WebKitWidgets
  Qt5::Network
  Qt5::PrintSupport
  Qt5::Qscintilla
  ${OpenMP_LIBRARIES}
  ${CxxTest_LIBRARIES}
  ${OpenCascade_LIBRARIES}
  ${Eigen3_LIBRARIES})
target_include_directories(
  boost_example
  PUBLIC ${Boost_INCLUDE_DIRS}
         ${PYTHON_INCLUDE_DIRS}
         ${TBB_INCLUDE_DIRS}
         ${Nexus_INCLUDE_DIRS}
         ${GSL_INCLUDE_DIRS}
         # ${JsonCPP_INCLUDE_DIRS} ${LibRDKafka_INCLUDE_DIRS}
         # ${Qt5_INCLUDE_DIRS}
         ${QSCINTILLA_QT5_INCLUDE_DIRS}
         # ${OpenMP_INCLUDE_DIRS}
         ${CxxTest_INCLUDE_DIRS}
  # ${OpenCascade_INCLUDE_DIRS} ${Eigen3_INCLUDE_DIRS}
)
