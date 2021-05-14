#!/bin/bash

mkdir build-conda
cd build-conda

cmake \
    -G Ninja \
    -DCMAKE_CXX_STANDARD=17\
    -DCMAKE_OSX_SYSROOT=${CONDA_BUILD_SYSROOT} \
    -DCMAKE_INSTALL_PREFIX=$PREFIX \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DBUILD_ALL=OFF \
    -DQT_TEST=ON \
    ..

ninja
ninja install
