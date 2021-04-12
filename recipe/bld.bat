mkdir build-conda
cd build-conda

cmake ^
    -DCMAKE_CXX_STANDARD=17 ^
    -G"Visual Studio 16 2019" ..


cmake  --build . 