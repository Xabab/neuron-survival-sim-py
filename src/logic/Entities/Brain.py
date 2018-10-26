import copy

import numpy as np
from engine.GameConstants import defaultHiddenLayersNeuronCount, BRAIN_INIT_RANGE, MUTAGEN_MULTIPLIER
from numpy.random import random


class Brain:
    def __init__(self, inputLayerNeurons: [str],
                 outputLayerNeurons: [str],
                 hiddenLayersNeuronCount: [int] = defaultHiddenLayersNeuronCount):

        # print("init:")
        # traceback.print_stack()

        self.inputsNames = inputLayerNeurons
        self.inputsNames.append("Bias (1)")
        self.outputsNames = outputLayerNeurons

        self.weights = []
        self.neuronLayers = []

        # print(len(hiddenLayersNeuronCount))
        # print(self.neuronLayers)

        self.neuronLayers.append(np.zeros((1, len(inputLayerNeurons))))

        for i in range(0, len(hiddenLayersNeuronCount)):
            # print("hidden layer", i)

            self.neuronLayers.append(np.zeros((1, hiddenLayersNeuronCount[i] + 1)))  # '+ 1' bias

        self.neuronLayers.append(np.zeros((1, len(outputLayerNeurons))))

        for i in range(0, len(self.neuronLayers) - 1):
            self.weights.append(np.zeros((len(self.neuronLayers[i][0]), len(self.neuronLayers[i + 1][0]))))

    #            for k in range(0, len(self.weights)):
    #                for j in range(0, len(self.weights[k])):
    #                    for n in range(0, len(self.weights[k][j])):
    #                        self.weights[k][j][n] = (random() * 2 - 1) * BRAIN_INIT_RANGE

    # print(self.neuronLayers, "neuron layers")
    # print(self.weights, "weights")

    @staticmethod
    def copy(class_instance):
        return copy.deepcopy(class_instance)

    def initRandom(self, min=-BRAIN_INIT_RANGE, max=BRAIN_INIT_RANGE):
        # print("init random brain")
        for n in range(0, len(self.weights)):
            for i in range(0, len(self.weights[n])):
                for j in range(0, len(self.weights[n][i])):
                    self.weights[n][i][j] = random() * (max - min) + min
        # print(self.weights)

    def calculate(self):
        # print("calculate")
        self.neuronLayers[0][0][len(self.neuronLayers[0][0]) - 1] = 1.
        for i in range(0, len(self.weights)):
            self.neuronLayers[i + 1] = np.dot(self.neuronLayers[i], self.weights[i])
            for j in range(0, len(self.neuronLayers[i + 1][0])):
                self.neuronLayers[i + 1][0][j] = np.tanh(self.neuronLayers[i + 1][0][j])
                if (i != len(self.weights) - 1) & (j == len(self.neuronLayers[i + 1][0]) - 1):  # setting bias back to 1
                    self.neuronLayers[i + 1][0][j] = 1

    def updateInputs(self, input: []):
        if len(input) != len(self.neuronLayers[0][0]) - 1:  # '- 1' bias
            print("input error!", len(input), len(self.neuronLayers[0]) - 1)
            return

        for i in range(0, len(input)):
            self.neuronLayers[0][0][i] = input[i]

    def mutate(self):
        for n in range(0, len(self.weights)):
            for i in range(0, len(self.weights[n])):
                for j in range(0, len(self.weights[n][i])):
                    self.weights[n][i][j] += (random() * 2 - 1) * MUTAGEN_MULTIPLIER
