"""Class for Inception V3 classsifier."""
from keras.applications import inception_v3
import numpy as np

from core.classifiers import BaseClassifier

class Inception(BaseClassifier.BaseClassifier):
    def _init__(self):
        super(Inception, self).__init__()

    def _generate_model(self):
        model = inception_v3.InceptionV3(weights='imagenet', include_top=False)

    def _restore_model_params(self):
        pass

    @attribute
    def _classifier_name(self):
        return 'Inception'

    def predict(self, frame):
        return model.predict(np.expand_dims(frame, 0))
