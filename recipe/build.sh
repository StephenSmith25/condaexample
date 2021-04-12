#!/bin/bash

mkdir build-conda
cd build-conda

cmake \
    -G Ninja \
    -DCMAKE_CXX_STANDARD=17\
    -DCMAKE_OSX_DEPLOYMENT_TARGET=10.14\
    ..

cmake  --build . 
