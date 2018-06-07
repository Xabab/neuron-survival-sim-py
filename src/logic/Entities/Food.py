from numpy.random import random

from src.engine.GameConstants import *
from src.logic.Entities.FoodPiece import FoodPiece

food = []


def startSpawn(food = food):
    for i in range(0, FOOD_COUNT):
        food.append(FoodPiece(random() * FIELD_SIZE_X, random() * FIELD_SIZE_Y))

