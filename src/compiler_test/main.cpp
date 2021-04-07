#include <iostream>
template <typename... Args> auto sum(Args... args) { return (args + ...); }

int main() {
  auto val = sum(1, 2, 4, 5, 5, 6);
  std::cout << val << "\n";
  return val;
}
