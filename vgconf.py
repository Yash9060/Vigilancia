"""Configuration parameters and constants for Vigilancia."""

import os

# Base path where trained classifiers stored.
VIGILANCIA_PATH = os.path.abspath('.')
CLASSIFIER_DATA_PATH = os.path.join(VIGILANCIA_PATH, 'data', 'classifiers')
EXTRAS_PATH = os.path.join(VIGILANCIA_PATH, 'extras')

# Extra module names.
DARKFLOW_MODULE_NAME = 'darkflow'
