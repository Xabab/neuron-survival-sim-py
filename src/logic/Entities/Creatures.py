from numpy.random import random

from src.engine.GameConstants import *
from src.logic.Entities.Creature import Creature

creatures = []


def startSpawn(creatures = creatures):
    for i in range(0, MIN_CREATURES_COUNT):
        creatures.append(Creature(random() * FIELD_SIZE_X, random() * FIELD_SIZE_Y))
