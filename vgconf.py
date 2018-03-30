"""Configuration parameters and constants for Vigilancia."""

import os

# Base path where trained classifiers stored.
VIGILANCIA_PATH = os.path.abspath('.')
CLASSIFIER_DATA_PATH = os.path.join(VIGILANCIA_PATH, 'data', 'classifiers')
EXTRAS_PATH = os.path.join(VIGILANCIA_PATH, 'extras')

# Extra module names.
DARKFLOW_MODULE_NAME = 'darkflow'

# Default values.
DEFAULT_YOLO_SAMPLE_RATE = 5
DEFAULT_FIREARM_SAMPLE_RATE = 5
DEFAULT_INCEPTION_SAMPLE_RATE = 15
ACTIVITY_DETECTOR_LENGTH = 4

# Set default YOLO classifier. It can be either 'tiny-yolo-coco' or
# 'yolo-coco'.
DEFAULT_YOLO_CLASSIFIER = 'tiny-yolo-coco'
# Set default Firearm classifier. It can be either 'FirearmDetectorTiny' or
# 'FirearmDetector'.
DEFAULT_FIREARM_DETECTOR = 'FirearmDetector'
# Set default Event classifier. It can be either 'EventDetectorTiny' or
# 'EventDetector'.
DEFAULT_EVENT_DETECTOR = 'EventDetector'

# Classifier constants.
ACTIVITY_DETECTION_THRESHOLD = 0.95
EVENT_DETECTION_TOP_COUNT = 3
YOLO_THRESHOLD = 0.25
FIREARM_DETECTION_THRESHOLD = 0.45

# Normal and Abnormal Activity prediction strings.
ABNORMAL_ACTIVITY = 'Abnormal Activity'
NORMAL_ACTIVITY = 'Normal Activity'

# Flash the screen for given number of times when suspicious objects or events
# are detected.
DEFAULT_ALERT_FLASH_COUNT = 8

# Suspicious objects.
SUSPICIOUS_OBJECTS_LIST = ['pistol', 'knife']
SUSPICIOUS_EVENTS_LIST = [
    'Parade' ,'People_Marching' ,'Riot' ,'Raid',' Traffic' ,'Car_Racin' ,
    'Car_Accident' ,'Soldier_Firing' ,'Soldier_Patrol' ,'Soldier_Drilling' ,
    'Street_Battle']
SUSPICIOUS_ACTIVITY = ABNORMAL_ACTIVITY

# Audio alert file.
ALERT_BEEP_FILE = os.path.join(VIGILANCIA_PATH, 'data', 'sounds', 'beep.wav')
