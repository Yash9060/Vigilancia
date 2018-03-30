"""Class for Unusual Activity Detector."""
import json

from keras import layers, models
import numpy as np

from core.classifiers import BaseClassifier
import vgconf

class EventDetector(BaseClassifier.BaseClassifier):
    def __init__(self):
        if vgconf.DEFAULT_EVENT_DETECTOR == 'EventDetectorTiny':
            self.weights_file = 'EventDetectorTiny.h5'
            self.meta_file = 'EventDetectorTinyLabels.json'
            self.hidden_neurons = 250
            self.n_classes = 5
        elif vgconf.DEFAULT_EVENT_DETECTOR == 'EventDetector':
            self.weights_file = 'EventDetector.h5'
            self.meta_file = 'EventDetectorLabels.json'
            self.hidden_neurons = 800
            self.n_classes = 61
        super(EventDetector, self).__init__()

    def _generate_model(self):
        inp = layers.Input(shape=(2048,))
        x = layers.Dense(self.hidden_neurons, activation='sigmoid', name='fc1')(inp)
        x = layers.Dropout(0.5, name='fc1drop')(x)
        preds = layers.Dense(units=self.n_classes, activation='sigmoid')(x)
        self.model = models.Model(inputs=inp, outputs=preds)
        self.model.compile(
            optimizer='nadam', loss='categorical_crossentropy',
            metrics=['accuracy'])

    def get_class_name(self, predictions):
        prediction = predictions.argsort()[-vgconf.EVENT_DETECTION_TOP_COUNT:]
        events = []
        for p in prediction:
            events.append(self.meta_data[p])
        return events

    def _restore_model_params(self):
        self.model.load_weights(self._get_data_path(self.weights_file))
        json_data = json.loads(
            open(self._get_data_path(self.meta_file), 'r').read())
        keys = map(int, json_data.keys())
        values = json_data.values()
        self.meta_data = dict(zip(keys, values))

    @property
    def _classifier_name(self):
        return 'EventDetector'

    def predict(self, frame):
        predictions = self.model.predict(np.expand_dims(frame, 0))[0]
        return self.get_class_name(predictions)

    def close(self):
        pass
