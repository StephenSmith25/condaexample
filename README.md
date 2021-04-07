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


OSX

- Run the same instructions but this time point to the osx environment 
- One the environment is activate you can do ECHO $CC / echo $CXX, it'll point to the conda compilers
- run cmake, it should use the conda compilers


-- The C compiler identification is Clang 11.1.0
-- The CXX compiler identification is Clang 11.1.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/local/Caskroom/miniconda/base/envs/condatest-developer/bin/x86_64-apple-darwin13.4.0-clang - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/local/Caskroom/miniconda/base/envs/condatest-developer/bin/x86_64-apple-darwin13.4.0-clang++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Found Boost: /usr/local/Caskroom/miniconda/base/envs/condatest-developer/lib/cmake/Boost-1.75.0/BoostConfig.cmake (found version "1.75.0")  
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/name/conda/condawindows/build

- We can look at the full compile options by doing 'VERBOSE=1 make' which shows the following

cd /Users/stephensmith/conda/condawindows/build/src/stdlib_test && /usr/local/Cellar/cmake/3.19.7/bin/cmake -E cmake_link_script CMakeFiles/stdlib_example.dir/link.txt --verbose=1
/usr/local/Caskroom/miniconda/base/envs/condatest-developer/bin/x86_64-apple-darwin13.4.0-clang++ -march=core2 -mtune=haswell -mssse3 -ftree-vectorize -fPIC -fPIE -fstack-protector-strong -O2 -pipe -stdlib=libc++ -fvisibility-inlines-hidden -std=c++14 -fmessage-length=0 -isystem /usr/local/Caskroom/miniconda/base/envs/condatest-developer/include -isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX10.15.sdk -Wl,-search_paths_first -Wl,-headerpad_max_install_names -Wl,-pie -Wl,-headerpad_max_install_names -Wl,-dead_strip_dylibs -Wl,-rpath,/usr/local/Caskroom/miniconda/base/envs/condatest-developer/lib -L/usr/local/Caskroom/miniconda/base/envs/condatest-developer/lib CMakeFiles/stdlib_example.dir/main.cpp.o -o stdlib_example 

- Which looks like its picking up the runtime libs from the conda enviroment lib folder (e.g libc++ ect ect)
