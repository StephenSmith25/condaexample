// Copyright Louis Dionne 2013-2017
// Distributed under the Boost Software License, Version 1.0.
// (See accompanying file LICENSE.md or copy at
// http://boost.org/LICENSE_1_0.txt)
#include <iostream>
#include <boost/hana/basic_tuple.hpp>
#include <boost/hana/core/make.hpp>
#include <type_traits>
#include <boost/python.hpp>

// boost example from Louiis Dionne

namespace hana = boost::hana;
constexpr hana::basic_tuple<int, char, double> xs{ 1, '2', 3.3 };
constexpr auto ys = hana::make<hana::basic_tuple_tag>(1, '2', 3.3);
constexpr auto zs = hana::make_basic_tuple(1, '2', 3.3);
static_assert(std::is_same<decltype(ys), decltype(xs)>::value, "");
static_assert(std::is_same<decltype(zs), decltype(xs)>::value, "");

int main() {}

class Example {
    public:
    void foo() {
        std::cout << "foo" << "/n";
    }
    void bar(int bar) {
        for (int i = 0; i < bar; i++){
            std::cout << "bar";
        }
        std::cout << "/n";
    }
};

namespace BoostPythonExample{
// Boost python
void export_Example() {
  // Expose class and member-function.
  boost::python::class_<Example>("Example")
    .def("foo",  &Example::foo, boost::python::arg("self"), "foo")
    .def("bar", &Example::bar, boost::python::args("self", "bar"), "bar");
}
}