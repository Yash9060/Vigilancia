"""Main starting point of Vigilancia."""

# Do this before anything else.
import vg_config
vg_config.init()

# Start other things.
import cv2
import time

# Just sanity check.
from core.classifiers import YOLOClassifier

# Generate YOLO model.
yolo = YOLOClassifier.YOLO()
cap = cv2.VideoCapture(0)

elapsed = 0
sample_rate = 5
preds = []
start = time.time()

while True:
    ret, frame = cap.read()
    
    if elapsed % sample_rate == 0:
        sys.stdout.write('\r')
        sys.stdout.write('%.3f FPS' % (elapsed / (time.time() - start)))
        sys.stdout.flush()
        preds = yolo.predict(frame)
    
    for pred in preds:
        cv2.rectangle(
            frame, (pred['topleft']['x'], pred['topleft']['y']),
            (pred['bottomright']['x'], pred['bottomright']['y']),
            (0, 255, 0), 1)
    elapsed += 1
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print('\nHappy to Help!')
