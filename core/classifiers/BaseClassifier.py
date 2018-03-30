"""This is base class for all classifiers of Vigilancia."""

import abc
import os

import vgconf

class BaseClassifier(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._generate_model()
        self._restore_model_params()
    
    def _get_data_path(self, file_name):
        return os.path.join(
            vgconf.CLASSIFIER_DATA_PATH, self._classifier_name, file_name)

    @abc.abstractmethod
    def _restore_model_params(self, classifier_data):
        """This method should be implemented by respective classes."""
        pass
    
    @abc.abstractproperty
    def _classifier_name(self):
        """This method should return name of the model which will able to
        identify its model data."""
        pass
    
    @abc.abstractmethod
    def _generate_model(self):
        """Each class should create its classifier model in this method."""
        pass
    
    @abc.abstractmethod
    def predict(self, inputs):
        """This method performs and returns the prediction."""
        pass

    @abc.abstractmethod
    def close(self):
        """This method closes the active session of the classifier"""
        pass
