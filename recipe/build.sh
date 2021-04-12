#!/bin/bash

mkdir build
cd build

cmake \
    -G Ninja \
    -DCMAKE_CXX_STANDARD=17\
    -DCMAKE_OSX_DEPLOYMENT_TARGET=10.14\
    ..

ninja

