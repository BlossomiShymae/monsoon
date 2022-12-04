#! /bin/bash
# A shell script to build the main application into executables

version="0.0.0"
exe_name="monsoon"
debug_exe_name="monsoon-debug-console"

# Parse canonical version from Python source file
parse_version() {
    version=$(awk '/VERSION/' ./src/constants.py | cut -d '"' -f2)
}

# Setup names for the distributed executables
setup_executable_names() {
    exe_name="${exe_name}-${version}"
    debug_exe_name="${debug_exe_name}-${version}"
}

# Build the application
build() {
    pyinstaller src/monsoon.py --add-data "resources/images/*;resources/images" \
    --onefile --hidden-import "win32api" --hidden-import "dependency_injector.errors" \
    --hidden-import "six" --icon "monsoon.ico" -n "$debug_exe_name"
    
    pyinstaller src/monsoon.py --add-data "resources/images/*;resources/images" \
    --onefile --noconsole --hidden-import "win32api" \
    --hidden-import "dependency_injector.errors" --hidden-import "six" \
    --icon "monsoon.ico" -n "$exe_name"
}

parse_version
setup_executable_names
build

# Archive and compress source code
git archive -o dist/latest.zip HEAD