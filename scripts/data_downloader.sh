#!/bin/bash

# Download data for YOLO model.
CURR_DIR=$(pwd)

if [ "$PREFERRED_YOLO_MODEL" = "Tiny YOLO" ]; then
    echo "Checking Tiny YOLO files..."

    YOLO_CFG=$CURR_DIR/data/classifiers/YOLO/tiny-yolo-coco.cfg
    if [ ! -f $YOLO_CFG ]; then
        echo "Downloading Tiny YOLO config file..."
        wget "https://github.com/pjreddie/darknet/blob/master/cfg/tiny-yolo.cfg" -O $YOLO_CFG
    fi;

    YOLO_WGT=$CURR_DIR/data/classifiers/YOLO/tiny-yolo-coco.weights
    if [ ! -f $YOLO_WGT ]; then
        echo "Downloading Tiny YOLO weights file..."
        wget "https://pjreddie.com/media/files/tiny-yolo.weights" -O $YOLO_WGT
    fi;
    
    echo "Tiny YOLO model is available locally"
fi;
