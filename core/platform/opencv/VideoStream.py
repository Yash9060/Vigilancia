"""Class for reading from a video stream."""
import cv2
import os

class VideoStream(object):
    def __init__(self, filename=None):
        if filename and self._check_file_exists(filename):
            self.stream_name = filename
        else:
            # TODO: Use logger instead of print. Its way better and standard.
            print("File %s does not exist. Using webcam for prediction." % filename)
            self.stream_name = 0

        self.capture = cv2.VideoCapture(self.stream_name)
        self.ret = True
        self.frame = None
    
    def _check_file_exists(self, filename):
        return os.path.exists(filename)

    def read_next_frame(self):
        self.ret, self.frame = self.capture.read()
        return self.frame
    
    def is_next_frame_available(self):
        return self.ret

    def qt_preprocess(self, frame, frame_size):
        frame = cv2.resize(frame, frame_size)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
    
    def close(self):
        self.ret = False
        self.frame = None
        self.capture.release()
