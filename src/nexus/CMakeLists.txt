add_executable(nexus_example main.cpp)
target_link_libraries(nexus_example PRIVATE ${NEXUS_CPP_LIBRARIES})
target_include_directories(nexus_example PRIVATE ${NEXUS_INCLUDE_DIR})