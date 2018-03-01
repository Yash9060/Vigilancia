"""Class for Unusual Activity Detector."""
from keras import layers, models
import numpy as np

from core.classifiers import BaseClassifier

class EventDetector(BaseClassifier.BaseClassifier):
    def __init__(self):
        self.weights_file = 'EventDetector.h5'
        super(EventDetector, self).__init__()

    def _generate_model(self):
        inp = layers.Input(shape=(2048,))
        x = layers.Dense(800, activation='sigmoid', name='fc1')(inp)
        x = layers.Dropout(0.5, name='fc1drop')(x)
        preds = layers.Dense(units=61, activation='softmax')(x)
        self.model = models.Model(inputs=inp, outputs=preds)
        self.model.compile(
            optimizer='nadam', loss='categorical_crossentropy',
            metrics=['accuracy'])

    def _restore_model_params(self):
        self.model.load_weights(self._get_data_path(self.weights_file))

    @property
    def _classifier_name(self):
        return 'EventDetector'

    def predict(self, frame):
        return self.model.predict(np.expand_dims(frame, 0))[0]
