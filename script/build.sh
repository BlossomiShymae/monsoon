#! /bin/bash
# A shell script to build the main application into executables

version="0.0.0"
exe_name="monsoon"
debug_exe_name="monsoon-debug-console"

# Parse canonical version from Python source file
parse_version() {
    version=$(awk '/VERSION/' ./src/constants/monsoon.py | cut -d '"' -f2)
}

# Setup names for the distributed executables
setup_executable_names() {
    exe_name="${exe_name}-${version}"
    debug_exe_name="${debug_exe_name}-${version}"
}

# Build the application
build() {
    pyinstaller src/monsoon.py --onefile --hidden-import "win32api" --icon "monsoon.ico" -n "$debug_exe_name"
    pyinstaller src/monsoon.py --onefile --noconsole --hidden-import "win32api" --icon "monsoon.ico" -n "$exe_name"
}

parse_version
setup_executable_names
build

# Archive and compress source code
git archive -o dist/latest.zip HEAD