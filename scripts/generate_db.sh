# This file should be executed only when software is being installed for the
# first time. No need to run this in susbequent runs. 

PYTHON_CMD=python
version=$(echo $($PYTHON_CMD -V 2>&1) | sed -e 's/Python //g' | sed -e 's/.[0-9].*//g')
if [ ! $version -eq 3 ]; then
    PYTHON_CMD=python3
    version=$(echo $($PYTHON_CMD -V 2>&1) | sed -e 's/Python //g' | sed -e 's/.[0-9].*//g')
    if [ ! $version -eq 3 ]; then
        echo "Unknown python command. Please install Python 3."
    fi;
fi;

$PYTHON_CMD $(pwd)/scripts/GenerateDB.py
