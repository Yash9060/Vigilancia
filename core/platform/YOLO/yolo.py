"""Provides necessary functions for building YOLO model.""" 
from darkflow.net import build

def build_yolo_network(options):
    model = build.TFNet(options)
    return model
