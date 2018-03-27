#!/bin/bash

# Download data for YOLO model.
CURR_DIR=$(pwd)

if [ "$PREFERRED_YOLO_MODEL" = "Tiny YOLO" ]; then
    echo "Checking Tiny YOLO files..."

    YOLO_CFG=$CURR_DIR/data/classifiers/YOLO/tiny-yolo-coco.cfg
    if [ ! -f $YOLO_CFG ]; then
        echo "Downloading Tiny YOLO config file..."
        wget "https://github.com/pjreddie/darknet/raw/master/cfg/tiny-yolo.cfg" -O $YOLO_CFG
    fi;

    YOLO_WGT=$CURR_DIR/data/classifiers/YOLO/tiny-yolo-coco.weights
    if [ ! -f $YOLO_WGT ]; then
        echo "Downloading Tiny YOLO weights file..."
        wget "https://pjreddie.com/media/files/tiny-yolo.weights" -O $YOLO_WGT
    fi;
    
    echo "Tiny YOLO model is available locally"
fi;

if [ "$PREFERRED_YOLO_MODEL" = "YOLO" ]; then
    echo "Checking YOLO files..."

    YOLO_CFG=$CURR_DIR/data/classifiers/YOLO/yolo-coco.cfg
    if [ ! -f $YOLO_CFG ]; then
        echo "Downloading YOLO config file..."
        wget "https://github.com/pjreddie/darknet/raw/master/cfg/yolo.cfg" -O $YOLO_CFG
    fi;

    YOLO_WGT=$CURR_DIR/data/classifiers/YOLO/yolo-coco.weights
    if [ ! -f $YOLO_WGT ]; then
        echo "Downloading YOLO weights file..."
        wget "https://pjreddie.com/media/files/yolo.weights" -O $YOLO_WGT
    fi;
    
    echo "YOLO model is available locally"
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
if [ ! -f $EVENT_DETECTOR_WGT/EventDetector.h5 ]; then
    if [ ! -d $EVENT_DETECTOR_WGT ]; then
        mkdir $EVENT_DETECTOR_WGT
    fi;
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

if [ "$PREFERRED_FIREARM_MODEL" = "FirearmDetectorTiny" ]; then
    echo "Checking FirearmDetectorTiny files..."

    FIREARM_META=$CURR_DIR/data/classifiers/FirearmDetector/FirearmDetectorTiny.meta
    if [ ! -f $FIREARM_META ]; then
        echo "Downloading FirearmDetectorTiny meta file..."
        wget "https://github.com/prasanna08/VigilanciaWeights/raw/master/FirearmDetector/FirearmDetectorTiny.meta" -O $FIREARM_META
    fi;

    FIREARM_WGT=$CURR_DIR/data/classifiers/FirearmDetector/FirearmDetectorTiny.pb
    if [ ! -f $FIREARM_WGT ]; then
        echo "Downloading FirearmDetectorTiny weights file..."
        wget "https://github.com/prasanna08/VigilanciaWeights/raw/master/FirearmDetector/FirearmDetectorTiny.pb" -O $FIREARM_WGT
    fi;
    
    echo "FirearmDetectorTiny model is available locally"
fi;

if [ "$PREFERRED_FIREARM_MODEL" = "FirearmDetector" ]; then
    echo "Checking FirearmDetector files..."

    FIREARM_META=$CURR_DIR/data/classifiers/FirearmDetector/FirearmDetector.meta
    if [ ! -f $FIREARM_META ]; then
        echo "Downloading FirearmDetector meta file..."
        wget "https://github.com/prasanna08/VigilanciaWeights/raw/master/FirearmDetector/FirearmDetector.meta" -O $FIREARM_META
    fi;

    FIREARM_WGT=$CURR_DIR/data/classifiers/FirearmDetector/FirearmDetector.pb
    if [ ! -f $FIREARM_WGT ]; then
        FIREARM_WGT_1=$CURR_DIR/data/classifiers/FirearmDetector/FirearmDetector1
        FIREARM_WGT_2=$CURR_DIR/data/classifiers/FirearmDetector/FirearmDetector2
        echo "Downloading FirearmDetector weights file..."
        wget "https://github.com/prasanna08/VigilanciaWeights/raw/master/FirearmDetector/FirearmDetector1" -O $FIREARM_WGT_1
        wget "https://github.com/prasanna08/VigilanciaWeights/raw/master/FirearmDetector/FirearmDetector2" -O $FIREARM_WGT_2
        cat $FIREARM_WGT_1 $FIREARM_WGT_2 > $FIREARM_WGT
        rm FIREARM_WGT_1 FIREARM_WGT_2
    fi;
    
    echo "FirearmDetector model is available locally"
fi;
