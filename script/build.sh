#! /bin/bash

# Build the application
pyinstaller src/monsoon.py --onefile --hidden-import "win32api" --icon "monsoon.ico" -n "monsoon-debug-console"
pyinstaller src/monsoon.py --onefile --noconsole --hidden-import "win32api" --icon "monsoon.ico"

# Archive and compress redistributables
git archive -o dist/latest.zip HEAD