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

INCEPTION_WGT=$CURR_DIR/data/classifiers/Inception
echo "Checking Inception files..."
if [ ! -d $INCEPTION_WGT ]; then
    mkdir $INCEPTION_WGT
    wget "https://github.com/prasanna08/VigilanciaWeights/raw/master/Inception/Inception.pb" -O $INCEPTION_WGT/Inception.pb
fi;
echo "Inception weights are available locally"

EVENT_DETECTOR_WGT=$CURR_DIR/data/classifiers/EventDetector
echo "Checking Event Detector files..."
if [ ! -d $EVENT_DETECTOR_WGT ]; then
    mkdir $EVENT_DETECTOR_WGT
    wget "https://github.com/prasanna08/VigilanciaWeights/raw/master/EventDetector/EventDetector.h5" -O $EVENT_DETECTOR_WGT/EventDetector.h5
fi;
echo "Event Detector weights are available locally"

UNUSUAL_ACTIVITY_DETECTOR_WGT=$CURR_DIR/data/classifiers/UnusualActivityDetector
echo "Checking Unusual Activity Detector files..."
if [ ! -d $UNUSUAL_ACTIVITY_DETECTOR_WGT ]; then
    mkdir $UNUSUAL_ACTIVITY_DETECTOR_WGT
    wget "https://github.com/prasanna08/VigilanciaWeights/raw/master/UnusualActivityDetector/UnusualActivityDetector.h5" -O $UNUSUAL_ACTIVITY_DETECTOR_WGT/UnusualActivityDetector.h5
fi;
echo "Unusual Activity Detector weights are available locally"
