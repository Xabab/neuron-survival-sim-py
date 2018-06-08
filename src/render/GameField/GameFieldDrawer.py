from src.engine.GameConstants import *
from src.logic.Game import Game
from src.render.Shapes import drawEfCircle

g = Game()

def drawGameField():
    if len(g.creatures) != 0:
        drawCreatures()

    if len(g.food) != 0:
        drawFood()


def drawCreatures():
    for i in range(0, len(g.creatures)):
        drawEfCircle(FIELD_X_OFFSET + g.creatures[i].xy.x, g.creatures[i].xy.y, CREATURE_SIZE, 10, 0, 1, 0)


def drawFood():
    for i in range(0, len(g.food)):
        drawEfCircle(FIELD_X_OFFSET + g.food[i].xy.x, g.food[i].xy.y, 2, 4, 1, 1, 0.3)
