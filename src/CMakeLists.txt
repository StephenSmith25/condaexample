set(SOURCE_FILES
     example.cpp)

add_executable(intro example.cpp)
target_link_libraries(
  intro
  PRIVATE Boost::boost)