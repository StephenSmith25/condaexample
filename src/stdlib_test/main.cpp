#include <any>
#include <iostream>
#include <optional>
#include <variant>

template <class... Ts> struct overload : Ts... { using Ts::operator()...; };
template <class... Ts> overload(Ts...) -> overload<Ts...>;


// test some c++17 library features
int main() {
  std::optional<int> opt;
  opt = 2;
  std::cout << "Opt has value" << *opt << "\n";
  std::any any;
  double d = 3.14;
  any = d;
  std::cout << std::any_cast<double>(any) << "\n";

  std::variant<int, double, bool> var;
  var = false;

  std::visit(overload{[](const int &i) {
                        std::cout << "int"
                                  << "\n";
                      },
                      [](const double &i) {
                        std::cout << "double"
                                  << "\n";
                      },
                      [](const bool &i) {
                        std::cout << "bool"
                                  << "\n";
                      }},
             var);
  return 0;
}
