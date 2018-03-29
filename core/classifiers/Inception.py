"""Class for Inception V3 classsifier."""
import tensorflow as tf
import numpy as np

from core.classifiers import BaseClassifier

class Inception(BaseClassifier.BaseClassifier):
    def __init__(self, get_pool_output=True):
        self.model_file = 'Inception.pb'
        super(Inception, self).__init__()
        self.session = tf.Session()
        self.op_layer = self.session.graph.get_tensor_by_name('inception/pool_3:0')
        self.softmax_layer = self.session.graph.get_tensor_by_name('inception/softmax:0')
        self.inception_input_shape = (299, 299, 3)
        self.is_pool_output = get_pool_output
        self.inception_input_layer = 'inception/DecodeJpeg:0'

    def _generate_model(self):
        f = tf.gfile.FastGFile(self._get_data_path(self.model_file), 'rb')
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='inception')

    def _restore_model_params(self):
        pass
    
    def _check_and_fix_shape(self, frame):
        if frame.shape != self.inception_input_shape:
            frame = cv2.resize(frame, inception_input_shape)
        return frame

    def pool_output(self, frame):
        op = self.session.run(
            self.op_layer,
            {self.inception_input_layer: frame})
        return np.squeeze(op)
    
    def imagenet_prediction(self, frame):
        op = self.session.run(
            self.softmax_layer,
            {self.inception_input_layer: frame})
        return np.squeeze(op)

    @property
    def _classifier_name(self):
        return 'Inception'

    def predict(self, frame):
        #frame = self._check_and_fix_shape(frame)
        if self.is_pool_output:
            return self.pool_output(frame)
        else:
            return self.imagenet_prediction(frame)

    def close(self):
        self.session.close()