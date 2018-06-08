from numpy.random import random

from src.engine.GameConstants import *
from src.logic import Vector2d


class FoodPiece:

    xy: Vector2d

    def __init__(self, x: float = random() * FIELD_SIZE_X, y: float = random() * FIELD_SIZE_Y):
        self.xy = Vector2d.Vector2d(x, y)
