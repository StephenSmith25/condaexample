find_package(TBB REQUIRED)

find_package(Poco 1.10.1 REQUIRED)

# HDF5
find_package(ZLIB REQUIRED)
find_package(HDF5 COMPONENTS CXX HL REQUIRED)

find_package(JemallocLib)

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

find_package(Git REQUIRED)

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
  all_cpp_lib_check_test
  PUBLIC ${Boost_INCLUDE_DIRS}
         ${PYTHON_INCLUDE_DIRS}
         ${TBB_INCLUDE_DIRS}
         ${NEXUS_INCLUDE_DIRS}
         ${GSL_INCLUDE_DIRS}
         ${QSCINTILLA_QT5_INCLUDE_DIRS}
         ${CxxTest_INCLUDE_DIRS}
)
