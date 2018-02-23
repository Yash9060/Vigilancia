# Download darkflow.
echo "Checking necessary dependencies..."
CURR_DIR=$(pwd)
if [ ! -d $CURR_DIR/extras/darkflow ]; then
    echo "Downloading darkflow..."
    wget "https://github.com/prasanna08/darkflow/archive/master.zip" -v -O $CURR_DIR/extras/master.zip
    unzip $CURR_DIR/extras/master.zip -d $CURR_DIR/extras/
    mv $CURR_DIR/extras/darkflow-master $CURR_DIR/extras/darkflow
    rm $CURR_DIR/extras/master.zip
    cd $CURR_DIR/extras/darkflow
    # Compile darkflow.
    bash setup.sh
    cd $CURR_DIR
fi;
echo "dependencies check finished"

PYTHON_CMD=python
version=$(echo $($PYTHON_CMD -V 2>&1) | sed -e 's/Python //g' | sed -e 's/.[0-9].*//g')
if [ ! $version -eq 3 ]; then
    PYTHON_CMD=python3
    version=$(echo $($PYTHON_CMD -V 2>&1) | sed -e 's/Python //g' | sed -e 's/.[0-9].*//g')
    if [ ! $version -eq 3 ]; then
        echo "Unknown python command. Please install Python 3."
    fi;
fi;

export PYTHON_CMD
source $(dirname $0)/metadata.sh
source $(dirname $0)/data_downloader.sh
