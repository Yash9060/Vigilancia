"""Class for reading from a video stream."""
import cv2
import os

class VideoStream(object):
    WEBCAM_STREAM = '/dev/video0'
    def __init__(self, filename=None):
        if filename and self._check_file_exists(filename):
            self.stream_name = filename
        else:
            # TODO: Use logger instead of print. Its way better and standard.
            print("File %s does not exist. Using webcam for prediction." % filename)
            self.stream_name = self.WEBCAM_STREAM

        self.capture = cv2.VideoCapture(self.stream_name)
        self.ret = True
        self.frame = None
        self.is_closed = False

    def _flip_frame(self, frame):
        frame = cv2.flip(frame, 1)
        return frame

    def _check_file_exists(self, filename):
        return os.path.exists(filename)

    def read_next_frame(self):
        self.ret, self.frame = self.capture.read()
        if self.stream_name == self.WEBCAM_STREAM:
            self.frame = self._flip_frame(self.frame)
        return self.frame
    
    def is_next_frame_available(self):
        return self.ret

    def qt_preprocess(self, frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
    
    def close(self):
        if not self.is_closed:
            self.ret = False
            self.frame = None
            self.capture.release()
            self.is_closed = True
