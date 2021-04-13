#!/bin/bash

mkdir build-conda
cd build-conda

cmake \
    -G Ninja \
    -DCMAKE_CXX_STANDARD=17\
    -DCMAKE_OSX_SYSROOT=${CONDA_BUILD_SYSROOT} \
    ..

cmake  --build . 
