"""Bounding Box plotter class."""
import math

import cv2

class BoxPlotter(object):
    def __init__(self, labels=[]):
        self.labels = labels
        self.n_classes = len(labels)
        self.colors = []
        self.labels_to_colors = []
        self.default_color = (255, 0, 0)

    def add_labels(self, labels):
        self.labels.extend(labels)
        self.n_classes = len(self.labels)
        self._generate_colors()
        self._generate_labels_to_colors()

    def _generate_colors(self):
        base = int(math.ceil(pow(self.n_classes, 1.0/3)))
        base_sqr = base * base
        self.colors = []
        for i in range(len(self.labels)):
            blue = abs(2 - i / base_sqr)
            red = abs(2 - (i % base_sqr) / base)
            green= abs(2 - (i % base_sqr) % base)
            self.colors.append((blue * 127, red * 127, green * 127))

    def _generate_labels_to_colors(self):
        if not self.colors:
            self._generate_colors()
        self.labels_to_colors = dict(zip(self.labels, self.colors))

    def _get_color_for_label(self, label):
        if not self.labels_to_colors:
            self._generate_labels_to_colors()
        if label not in self.labels_to_colors:
            return self.default_color
        return self.labels_to_colors[label]

    def plot_bboxes(self, img, out):
        for pred in out:
            cv2.rectangle(
                img, (pred['topleft']['x'], pred['topleft']['y']),
                (pred['bottomright']['x'], pred['bottomright']['y']),
                self._get_color_for_label(pred['label']), 1)
            cv2.putText(
                img, pred['label'] + ' ' + str(pred['confidence']),
                (pred['topleft']['x'], pred['topleft']['y'] - 13),
                cv2.FONT_HERSHEY_SIMPLEX, 1e-3 * img.shape[0],
                self._get_color_for_label(pred['label']), 1)
        return img
