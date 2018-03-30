"""Class for Firearm Detector."""
import json
import os

from core.classifiers import BaseClassifier
from core.platform.darkflow import darkflow
import vgconf

class FirearmDetector(BaseClassifier.BaseClassifier):
    def __init__(self):
        self.config_file = ('%s.json' % vgconf.DEFAULT_FIREARM_DETECTOR)
        self.firearm_options = {
            'gpu': 1.0,
            'gpuName': '/device:GPU:0',
            'threshold': vgconf.FIREARM_DETECTION_THRESHOLD,
            'config': os.path.join(
                vgconf.EXTRAS_PATH, vgconf.DARKFLOW_MODULE_NAME, 'cfg')
        }
        self.labels = []
        super(FirearmDetector, self).__init__()
    
    @property
    def _classifier_name(self):
        return 'FirearmDetector'

    def _restore_model_params(self):
        pass

    def _generate_model(self):
        conf_path = self._get_data_path(self.config_file)
        firearm_conf = json.loads(open(conf_path, 'r').read())
        self.pb_path = self._get_data_path(firearm_conf['pb'])
        self.meta_path = self._get_data_path(firearm_conf['meta'])
        self.offset = firearm_conf['offset']
        self.labels_file =self._get_data_path(firearm_conf['labels'])
        self.firearm_options.update({
            'pbLoad': self.pb_path,
            'metaLoad': self.meta_path,
            'offset': self.offset,
            'labels': self.labels_file
        })
        self.model = darkflow.build_network(self.firearm_options)
        self.n_classes = firearm_conf['classes']

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
