"""Class for Unusual Activity Detector."""
from keras import layers, models
import numpy as np

from core.classifiers import BaseClassifier
import vgconf

class UnusualActivityDetector(BaseClassifier.BaseClassifier):
    def __init__(self):
        self.weights_file = 'UnusualActivityDetector.h5'
        super(UnusualActivityDetector, self).__init__()

    def _generate_model(self):
        inp = layers.Input(shape=(4, 2048), name='inputs')
        x = layers.LSTM(20, name='lstm')(inp)
        preds = layers.Dense(units=1, activation="sigmoid", name='outputs')(x)
        self.model = models.Model(inputs=inp, outputs=preds)
        self.model.compile(
            optimizer='adam', loss='binary_crossentropy',
            metrics=['accuracy'])

    def get_class_name(self, predictions):
        prediction = predictions[0]
        if prediction > vgconf.ACTIVITY_DETECTION_THRESHOLD:
            return vgconf.ABNORMAL_ACTIVITY
        else:
            return vgconf.NORMAL_ACTIVITY

    def _restore_model_params(self):
        self.model.load_weights(self._get_data_path(self.weights_file))

    @property
    def _classifier_name(self):
        return 'UnusualActivityDetector'

    def predict(self, frame):
        predictions = self.model.predict(np.expand_dims(frame, 0))[0]
        return self.get_class_name(predictions)

    def close(self):
        pass
