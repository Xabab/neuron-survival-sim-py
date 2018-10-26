import copy
from math import sin, cos, pi, sqrt

from engine.GameConstants import *
from logic.Entities.Brain import Brain
from logic.Vector2d import Vector2d
from numpy.random import random


# todo fix birth

class Creature(object):
    def __init__(self, x: float, y: float):

        self.xy = Vector2d(x, y)
        self.speed = Vector2d(0., 0.)

        self.fitness = STARTING_FITNESS

        self.direction = ((random() * 2) - 1) * pi * 2

        self.brain = Brain(["Food dist", "Food dir", "Fitness", "Speed"],
                           ["Eat (not used)", "Accelerate", "Turn", "Birth"])
        self.brain.initRandom()

        self.debug_info = [0, 0, 0, 0]

    def Child(self):
        temp = copy.deepcopy(self)

        temp.speed = Vector2d(0., 0.)
        temp.fitness = STARTING_FITNESS
        temp.direction = ((random() * 2) - 1) * pi * 2
        temp.brain.mutate()

        return temp

    def giveBirth(self):
        self.fitness -= BIRTH_FITNESS_COST

        return self.Child()

    def updateInfo(self, inputs: [float]):
        self.debug_info = inputs

    def updateMoving(self):
        self.direction += CREATURE_TURNING_SPEED * self.brain.neuronLayers[len(self.brain.neuronLayers) - 1][0][2]

        if self.direction > pi:
            self.direction -= 2 * pi
        if self.direction < -pi:
            self.direction += 2 * pi

        x = self.speed.x * (1 - SURFACE_ROUGHNESS) + \
            ACCELERATION * self.brain.neuronLayers[len(self.brain.neuronLayers) - 1][0][1] * cos(self.direction)
        y = self.speed.y * (1 - SURFACE_ROUGHNESS) + \
            ACCELERATION * self.brain.neuronLayers[len(self.brain.neuronLayers) - 1][0][1] * sin(self.direction)
        speed = sqrt(x * x + y * y)

        # print(self.speed.x, self.speed.y)

        if speed > CREATURE_SPEED:
            x *= CREATURE_SPEED / speed
            y *= CREATURE_SPEED / speed

        self.speed.x = x
        self.speed.y = y

        self.fitness -= abs(self.brain.neuronLayers[len(self.brain.neuronLayers) - 1][0][2]) * FOOD_PER_RAD \
                        + speed * FOOD_PER_PX + FITNESS_DEGRADATION

    def move(self):
        self.xy.add(self.speed)

    def updateInputs(self, input: []):
        self.brain.updateInputs(input)

    def updateCreature(self):
        self.brain.calculate()
        self.updateMoving()
        self.move()

    def feed(self, f: float):
        self.fitness += f
