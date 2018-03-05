"""Main starting point of Vigilancia."""

# Do this before anything else.
import vg_config
vg_config.init()

# Start other things.
import cv2
import time
import sys

# Just sanity check.
from core.domain import SuspicionDetection
from core.platform.opencv import VideoStream

# Detector. Turn ON classifiers.
detector = SuspicionDetection.SuspicionDetection()
detector.enable_yolo_detection()
detector.enable_unusual_activity_detection()
stream = VideoStream.VideoStream(filename='../Crowd-Activity-All.avi')
preds = []
start = time.time()
elapsed = 0

while stream.is_next_frame_available():
    frame = stream.read_next_frame()
    detector.detect(frame)
    if elapsed % 5 == 0:
        sys.stdout.write('\r')
        preds = detector.get_activity_detector_prediction()
        if preds:
            print('Event: ', preds)
        sys.stdout.write(' %.3f FPS' % (elapsed / (time.time() - start)))
        sys.stdout.flush()
    frame = detector.plot_objects(frame)
    elapsed += 1
    cv2.imshow('video', frame)
    if cv2.waitKey(1000 // 30) & 0xFF == ord('q'):
        break

detector.close()
stream.close()
cv2.destroyAllWindows()

print('\nHappy to Help!')
