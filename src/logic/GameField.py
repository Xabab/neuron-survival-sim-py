from numpy.random import random

from src.engine.GameConstants import FOOD_COUNT, FIELD_SIZE_X, FIELD_SIZE_Y
from src.logic.Entities.Creature import Creature, MIN_CREATURES_COUNT
from src.logic.Entities.FoodPiece import FoodPiece


class GameField:

    def __init__(self):
        self.creatures = []
        self.food = []

    def init(self):
        self.startSpawn()

    def startSpawn(self):
        for i in range(0, MIN_CREATURES_COUNT):
            self.creatures.append(Creature())
        for i in range(0, FOOD_COUNT):
            self.food.append(FoodPiece(random() * FIELD_SIZE_X, random() * FIELD_SIZE_Y))
