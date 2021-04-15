find_package(PythonLibs 3.8 REQUIRED)
# Extract major/minor python version
string(REPLACE "." ";" VERSION_LIST ${PYTHONLIBS_VERSION_STRING})
list(GET VERSION_LIST 0 PYTHONLIBS_VERSION_MAJOR)                                                                                                                             
list(GET VERSION_LIST 1 PYTHONLIBS_VERSION_MINOR)
find_package(Boost COMPONENTS python${PYTHONLIBS_VERSION_MAJOR}${PYTHONLIBS_VERSION_MINOR} REQUIRED)
add_executable(boost_example main.cpp)
target_link_libraries(boost_example ${Boost_LIBRARIES} ${PYTHON_LIBRARIES})
target_include_directories(boost_example PRIVATE ${PYTHON_INCLUDE_DIRS})
