add_executable(boost_example main.cpp)
target_link_libraries(boost_example ${Boost_LIBRARIES} Python::Python)
target_include_directories(boost_example PRIVATE ${PYTHON_INCLUDE_DIRS})
