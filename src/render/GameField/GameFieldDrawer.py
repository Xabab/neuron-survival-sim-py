from src.engine.GameConstants import *
from src.logic.Entities import Creatures, Food
from src.render.Shapes import drawEfCircle


def drawGameField():
    if len(Creatures.creatures) != 0:
        drawCreatures()

    if len(Food.food) != 0:
        drawFood()


def drawCreatures():
    for i in range(0, len(Creatures.creatures)):
        drawEfCircle(FIELD_X_OFFSET + Creatures.creatures[i].xy.x, Creatures.creatures[i].xy.y, CREATURE_SIZE, 10, 0, 1, 0)


def drawFood():
    for i in range(0, len(Food.food)):
        drawEfCircle(FIELD_X_OFFSET + Food.food[i].xy.x, Food.food[i].xy.y, 3, 4, 1, 1, 0.3)