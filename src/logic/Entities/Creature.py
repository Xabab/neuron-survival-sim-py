import copy

import numpy as np
from numpy.core.umath import pi
from numpy.random import random

from src.engine.GameConstants import *
from src.logic.Entities.Brain import Brain
from src.logic.Vector2d import Vector2d


class Creature:

    xy: Vector2d
    speed: Vector2d

    fitness: float

    direction: float

    debug_info: [float]

    brain: Brain

    @classmethod
    def __init__(cls, x: float = random() * FIELD_SIZE_X, y: float = random() * FIELD_SIZE_Y):
        cls.xy = Vector2d(x, y)
        cls.speed = Vector2d(0., 0.)

        cls.fitness = STARTING_FITNESS

        cls.direction = ((random() * 2) - 1) * pi * 2

        cls.brain = Brain(["Food dist", "Food dir", "Fitness", "Speed"], ["Eat", "Accelerate", "Turn", "Birth"])
        cls.brain.initRandom()

        cls.debug_info = [None, None, None, None]

    @classmethod
    def Child(cls):
        temp = copy.deepcopy(cls)

        temp.speed = Vector2d(0., 0.)
        temp.fitness = STARTING_FITNESS
        temp.direction = ((random() * 2) - 1) * pi * 2
        temp.brain.mutate()

        return temp

    @classmethod
    def giveBirth(cls):
        cls.fitness -= BIRTH_FITNESS_COST

        return cls.Child()

    @classmethod
    def updateInfo(cls, inputs: [float]):
        cls.debug_info = inputs

    @classmethod
    def updateMoving(cls):
        cls.direction += CREATURE_TURNING_SPEED * cls.brain.neuronLayers[len(cls.brain.neuronLayers) - 1][0][1]

        if cls.direction > pi: cls.direction -= 2 * pi;
        if cls.direction < -pi: cls.direction += 2 * pi;

        x = cls.speed.x * (1 - SURFACE_ROUGHNESS) + ACCELERATION * \
            cls.brain.neuronLayers[len(cls.brain.neuronLayers) - 1][0][0] * np.cos(cls.direction)
        y = cls.speed.y * (1 - SURFACE_ROUGHNESS) + ACCELERATION * \
            cls.brain.neuronLayers[len(cls.brain.neuronLayers) - 1][0][0] * np.sin(cls.direction)
        speed = np.sqrt(x * x + y * y)

        if speed > CREATURE_SPEED:
            x *= CREATURE_SPEED / speed
            y *= CREATURE_SPEED / speed

        cls.speed.x = x
        cls.speed.y = y

        cls.fitness -= abs(cls.brain.neuronLayers[len(cls.brain.neuronLayers) - 1][0][1]) * FOOD_PER_RAD \
                       + speed * FOOD_PER_PX + FITNESS_DEGRADATION

    @classmethod
    def move(cls):
        cls.xy.add(cls.speed)

    @classmethod
    def updateInputs(cls, input: []):
        cls.brain.updateInputs(input)

    @classmethod
    def updateCreature(cls):
        cls.brain.calculate()
        cls.updateMoving()
        cls.move()

    @classmethod
    def feed(cls, f: float):
        cls.fitness += f

