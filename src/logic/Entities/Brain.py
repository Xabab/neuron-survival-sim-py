import copy
from random import random

import numpy as np

from src.engine.GameConstants import defaultHiddenLayersNeuronCount, BRAIN_INIT_RANGE, MUTAGEN_MULTIPLIER


class Brain:
    weights = []
    neuronLayers = []
    inputsNames = []
    outputsNames = []

    def __init__(self, inputLayerNeurons: [str], outputLayerNeurons: [str],
                 hiddenLayersNeuronCount: [int] = defaultHiddenLayersNeuronCount):
        self.inputsNames = inputLayerNeurons
        self.inputsNames.append("Bias (1)")
        self.outputsNames = outputLayerNeurons

        self.neuronLayers.append(np.empty((1, len(inputLayerNeurons))))

        for i in range(0, len(hiddenLayersNeuronCount)):
            self.neuronLayers.append(np.empty((1, hiddenLayersNeuronCount[i] + 1)))  # '+ 1' bias

        self.neuronLayers.append(np.empty((1, len(outputLayerNeurons))))

        for i in range(0, len(self.neuronLayers) - 1):
            self.weights.append(np.empty(len(self.neuronLayers[i]), np.empty(len(self.neuronLayers[i + 1]))))

    @staticmethod
    def copy(class_instance):
        return copy.deepcopy(class_instance)

    @classmethod
    def initRandom(cls, min=-BRAIN_INIT_RANGE, max=BRAIN_INIT_RANGE):
        for n in range(0, len(cls.weights)):
            for i in range(0, len(cls.weights[n])):
                for j in range(0, len(cls.weights[n][i])):
                    cls.weights[n][i][j](random() * (max - min) + min)

    @classmethod
    def calculate(cls):
        for i in range(0, len(cls.weights)):
            cls.neuronLayers[i + 1] = np.dot(cls.weights[i], cls.neuronLayers[i])
            for j in range(0, len(cls.neuronLayers[i + 1])):
                cls.neuronLayers[i + 1][0][j] = np.tanh(cls.neuronLayers[i + 1][0][j])
                if i != len(cls.weights) - 1:
                    cls.neuronLayers[i + 1][0][len(cls.neuronLayers[i + 1]) - 1] = 1  # setting bias back to 1

    @classmethod
    def updateInputs(cls, input: []):
        if len(input) != len(cls.neuronLayers[0]) - 1:  # '- 1' bias
            return

        for i in range(0, len(input)):
            cls.neuronLayers[0][0][i] = input[i]

    @classmethod
    def mutate(cls):
        for n in range(0, len(cls.weights)):
            for i in range(0, len(cls.weights[n])):
                for j in range(0, len(cls.weights[n][i])):
                    cls.weights[n][i][j] += (random() * 2 - 1) * MUTAGEN_MULTIPLIER
