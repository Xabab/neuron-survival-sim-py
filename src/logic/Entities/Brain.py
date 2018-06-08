import copy

import numpy as np
from numpy.random import uniform as random

from src.engine.GameConstants import defaultHiddenLayersNeuronCount, BRAIN_INIT_RANGE, MUTAGEN_MULTIPLIER


class Brain:

    def __init__(self, inputLayerNeurons: [str],
                 outputLayerNeurons: [str],
                 hiddenLayersNeuronCount: [int] = defaultHiddenLayersNeuronCount,
                 weights=None, neuronLayers=None):
        print("init:")
        self.inputsNames = inputLayerNeurons
        self.inputsNames.append("Bias (1)")
        self.outputsNames = outputLayerNeurons

        self.weights = []
        self.neuronLayers = []

        print(len(hiddenLayersNeuronCount))
        print(self.neuronLayers)

        self.neuronLayers.append(np.zeros((1, len(inputLayerNeurons))))

        for i in range(0, len(hiddenLayersNeuronCount)):
            print("hidden layer", i)

            self.neuronLayers.append(np.zeros((1, hiddenLayersNeuronCount[i] + 1)))  # '+ 1' bias

        self.neuronLayers.append(np.zeros((1, len(outputLayerNeurons))))

        for i in range(0, len(self.neuronLayers) - 1):
            self.weights.append(np.zeros((len(self.neuronLayers[i]), len(self.neuronLayers[i + 1]))))

    @staticmethod
    def copy(class_instance):
        return copy.deepcopy(class_instance)

    def initRandom(self, min=-BRAIN_INIT_RANGE, max=BRAIN_INIT_RANGE):
        for n in range(0, len(self.weights)):
            for i in range(0, len(self.weights[n])):
                for j in range(0, len(self.weights[n][i])):
                    self.weights[n][i][j] = random(0, 1) * (max - min) + min

    def calculate(self):
        print((len(self.weights), len(self.neuronLayers)))
        print(self.neuronLayers)
        for i in range(0, len(self.weights)):
            print((len(self.neuronLayers), i))
            self.neuronLayers[i + 1] = np.dot(self.weights[i], self.neuronLayers[i])
            for j in range(0, len(self.neuronLayers[i + 1])):
                self.neuronLayers[i + 1][0][j] = np.tanh(self.neuronLayers[i + 1][0][j])
                if i != len(self.weights) - 1:
                    self.neuronLayers[i + 1][0][len(self.neuronLayers[i + 1]) - 1] = 1  # setting bias back to 1

    def updateInputs(self, input: []):
        if len(input) != len(self.neuronLayers[0]) - 1:  # '- 1' bias
            return

        for i in range(0, len(input)):
            self.neuronLayers[0][0][i] = input[i]

    def mutate(self):
        for n in range(0, len(self.weights)):
            for i in range(0, len(self.weights[n])):
                for j in range(0, len(self.weights[n][i])):
                    self.weights[n][i][j] += (random(0, 1) * 2 - 1) * MUTAGEN_MULTIPLIER
