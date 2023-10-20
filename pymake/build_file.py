yaml_data = """
# This handles building the project

# Change to whatever will compile your c/c++ code. You can even use emscripten!
compiler: gcc  

# The main source file
source: src/main.cpp

# The name of the project, used for debugging.
name: App name 

# The output file.
output: app.exe

# Should the program run after building?
run: true 

# These are the flags that will be passed to the compiler, such as -std=c++17
flags:
    - std=c++17

# The c/c++ files that will be compiled in order.
files:
    - utils.cpp

# Where are the header files located?
includes:
    - include/

# Not to be confused with libraries, these are the paths to the libraries.
libs:
    - path/to/lib

# These are the libraries that will be linked to the project. Path must be specified in libs.
libraries: 
    - raylib

"""


def build_file(config_path):
    with open(config_path, 'w') as f:
        f.write(yaml_data)