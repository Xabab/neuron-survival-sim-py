from numpy.core.umath import sin, cos

from src.engine.GameConstants import *
from src.logic import Game
from src.render.Shapes import drawEfCircle, drawLine
from src.render.Text import text


class GameFieldDrawer:
    g = Game.g

    def drawGameField(self):
        if self.g.theChosenOne is not None:
            if self.g.theChosenOne.fitness < 0:
                self.g.theChosenOne = None
            else:
                self.drawChosenOne()

        if len(self.g.creatures) != 0:
            self.drawCreatures()

        if len(self.g.food) != 0:
            self.drawFood()

    def drawChosenOne(self):
        c = self.g.theChosenOne
        drawEfCircle(int(c.xy.x + FIELD_X_OFFSET), int(c.xy.y), int(CREATURE_SIZE * 2), 10, 0.2, 0.2, 0.5)

        text(20, 80, "Dir", 1, 1, 1)
        text(20, 90, str(c.direction), 1, 1, 1)

        text(20, 110, "Food dist", 1, 1, 1)
        text(20, 120, str(c.debug_info[0]), 1, 1, 1)

        text(20, 140, "Food dir", 1, 1, 1)
        text(20, 150, str(c.debug_info[1]), 1, 1, 1)

        text(20, 170, "Fit", 1, 1, 1)
        text(20, 180, str(c.fitness), 1, 1, 1)

        text(20, 200, "Speed", 1, 1, 1)
        text(20, 210, str(c.speed.length()), 1, 1, 1)

        x = 5
        for i in range(0, len(c.brain.neuronLayers)):
            y = 300
            for n in range(0, len(c.brain.neuronLayers[i][0])):
                text(x, y, str(round(c.brain.neuronLayers[i][0][n], 4)), 1, 1, 1)
                y += 10
            x += 40

    def drawCreatures(self):
        for i in range(0, len(self.g.creatures)):
            c = self.g.creatures[i]

            drawEfCircle(FIELD_X_OFFSET + c.xy.x, c.xy.y, CREATURE_SIZE, 10, 0, c.fitness / STARTING_FITNESS, 0)
            drawLine(int(FIELD_X_OFFSET + c.xy.x), int(c.xy.y),
                     int(FIELD_X_OFFSET + (c.xy.x + cos(c.direction) * CREATURE_SIZE)),
                     int((c.xy.y + sin(c.direction) * CREATURE_SIZE)), 1, 0.3, 0.3, 1)
            drawLine(int(FIELD_X_OFFSET + c.xy.x), int(c.xy.y),
                     int(FIELD_X_OFFSET + (c.xy.x + cos(c.debug_info[1]) * c.debug_info[0] + c.direction)),
                     int((c.xy.y + sin(c.debug_info[1]) * c.debug_info[0] + c.direction)), 1, 1, 0.3, 0.3)

    def drawFood(self):
        for i in range(0, len(self.g.food)):
            drawEfCircle(FIELD_X_OFFSET + self.g.food[i].xy.x, self.g.food[i].xy.y, 2, 4, 1, 1, 0.3)
