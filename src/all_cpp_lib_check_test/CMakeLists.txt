#include <tbb>
#include <boost>
#include <poco>
#include <nexus>
#include <hdf> // Hdf4
#include <hdf5>
#include <jemalloc>
#include <gsl>
#include <jsoncpp>
#include <kafka>
#include <qt>
#include <qtwebkit>
#include <qscintilla>

# find_package(tbb REQUIRED)
# find_package(boost REQUIRED)
# find_package(poco REQUIRED)
# find_package(nexus REQUIRED)
# find_package(hdf REQUIRED) # Hdf4
# find_package(hdf5 REQUIRED)
# find_package(jemalloc REQUIRED)
# find_package(gsl REQUIRED)
# find_package(jsoncpp REQUIRED)
# find_package(kafka REQUIRED)
# find_package(qt REQUIRED)
# find_package(qtwebkit REQUIRED)
# find_package(qscintilla REQUIRED)

add_executable(all_cpp_lib_check_test main.cpp)
target_link_libraries(all_cpp_lib_check_test Boost::boost)