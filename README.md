# Summary
This repository contains a test conda project using all the depdendencies required by Mantid https://www.mantidproject.org/

# Environment setup
To build this project you will require a conda instalation, for isntance miniconda. Once aquired, it would be worthwhile installing the mamba package manager using,
```
conda install mamba -n base -c conda-forge
```
You can now create a conda environment using
```
conda create -f condatest-developer-***.yml
```
where *** is replaced with your target OS. Now activate the environment
```
conda activate condatest-developer
```

# Build
You can now build all the projects with,
```
mkdir build
cd build
cmake ..
make -j4
```


