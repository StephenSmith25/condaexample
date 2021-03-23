Testing conda on windows. To use:
- Install miniconda3
- Open Anaconda prompt
- cd to this repo
- mkdir build
- cd build
- conda env create -f ../condatest-developer.yml
- conda activate condatest-developer
- cmake -G"Visual Studio 16 2019" ..
- open the project in visual studio and you should be able to build everything