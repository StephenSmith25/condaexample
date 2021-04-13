#include "napi.h"
#include "NeXusFile.hpp"

#include <iostream>


void writeFile(const std::string filename) {
    std::cout << "Creating a nexus file" << std::endl;
    NeXus::File file(filename, NXACC_CREATE);
    file.makeGroup("entry", "NXentry", true);
    file.closeGroup();
}

// test some c++17 library features
int main() {
    NXstatus a;
    writeFile("MyTestFile");
    return 0;
}
