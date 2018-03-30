"""Class for YOLO classifier."""
import json
import os

from core.classifiers import BaseClassifier
from core.platform.darkflow import darkflow
import vgconf

class YOLO(BaseClassifier.BaseClassifier):
    def __init__(self):
        self.config_file = ('%s.json' % vgconf.DEFAULT_YOLO_CLASSIFIER)
        self.yolo_options = {
            'gpu': 1.0,
            'gpuName': '/device:GPU:0',
            'threshold': vgconf.YOLO_THRESHOLD,
            'config': os.path.join(
                vgconf.EXTRAS_PATH, vgconf.DARKFLOW_MODULE_NAME, 'cfg')
        }
        self.labels = []
        super(YOLO, self).__init__()

    @property
    def _classifier_name(self):
        return 'YOLO'

    def _restore_model_params(self):
        pass

    def _generate_model(self):
        conf_path = self._get_data_path(self.config_file)
        yolo_conf = json.loads(open(conf_path, 'r').read())
        self.cfg_path = self._get_data_path(yolo_conf['config'])
        self.weights_path = self._get_data_path(yolo_conf['weights'])
        self.offset = yolo_conf['offset']
        self.yolo_options.update({
            'model': self.cfg_path,
            'load': self.weights_path,
            'offset': self.offset
        })
        self.model = darkflow.build_network(self.yolo_options)
        self.n_classes = yolo_conf['classes']
        self.labels_file =self._get_data_path(yolo_conf['labels'])

    def _process_labels_file(self):
        self.labels = []
        labels_file = open(self.labels_file, 'r')
        for label in labels_file.readlines():
            self.labels.append(label.strip())

    def get_labels(self):
        if not self.labels:
            self._process_labels_file()
        return self.labels

    def predict(self, frame):
        return self.model.return_predict(frame)

    def close(self):
        self.model.sess.close()
