mkdir build-conda
cd build-conda

cmake ^
    -DCMAKE_CXX_STANDARD=17 ^
    -G Ninja ..


cmake  --build . 