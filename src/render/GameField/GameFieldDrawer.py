from src.engine.GameConstants import *
from src.logic import Game
from src.render.Shapes import drawEfCircle


class GameFieldDrawer:
    g = Game.g

    def drawGameField(self):
        if len(self.g.creatures) != 0:
            self.drawCreatures()

        if len(self.g.food) != 0:
            self.drawFood()

    def drawCreatures(self):
        for i in range(0, len(self.g.creatures)):
            drawEfCircle(FIELD_X_OFFSET + self.g.creatures[i].xy.x, self.g.creatures[i].xy.y, CREATURE_SIZE, 10, 0, 1,
                         0)

    def drawFood(self):
        for i in range(0, len(self.g.food)):
            drawEfCircle(FIELD_X_OFFSET + self.g.food[i].xy.x, self.g.food[i].xy.y, 2, 4, 1, 1, 0.3)
