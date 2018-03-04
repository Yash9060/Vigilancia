"""Class for YOLO classifier."""
import json
import os

from core.classifiers import BaseClassifier
from core.platform.yolo import yolo
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
        self.model = yolo.build_yolo_network(self.yolo_options)
    
    def predict(self, frame):
        return self.model.return_predict(frame)
