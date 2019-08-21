from numpy.core.umath import sin, cos

from engine.GameConstants import *
from gui.Gui import drawGui
from logic import Game
from render.Shapes import drawEfCircle, drawLine, drawBox, GL_LINE_LOOP, GL_POLYGON
from render.Text import text


class GameDrawer:
    gameField = Game.g

    def drawGame(self):
        # field and creatures
        drawBox(0, 0, X, Y, GL_POLYGON, 0.2, 0.25, 0.2)

        self.drawGrid()

        if self.gameField.theChosenOne is not None:
            if self.gameField.theChosenOne.fitness < 0:
                self.gameField.theChosenOne = None
            else:
                self.drawChosenOne()

        if len(self.gameField.creatures) != 0:
            self.drawCreatures()

        if len(self.gameField.food) != 0:
            self.drawFood()

        # gui
        drawBox(0, 0, MENU_WIDTH, Y, GL_POLYGON, 0.4, 0.4, 0.43, 1)

        drawGui()

        if self.gameField.theChosenOne is not None:
            if self.gameField.theChosenOne.fitness < 0:
                self.gameField.theChosenOne = None
            else:
                self.drawTheChosenOneInfo()

    def drawChosenOne(self):
        c = self.gameField.theChosenOne

        if FOG_OF_WAR:
            cellX = int(c.xy.x / CELL_SIZE)
            cellY = int(c.xy.y / CELL_SIZE)

            sight = Game.Game.sightCircle

            for s in range(0, len(sight)):
                drawBox(int(FIELD_X_OFFSET + (cellX + sight[s][0]) * CELL_SIZE), int((cellY + sight[s][1]) * CELL_SIZE),
                        int(CELL_SIZE), int(CELL_SIZE),
                        GL_POLYGON, 0.5, 0.5, 0.2)
                drawBox(int(FIELD_X_OFFSET + (cellX + sight[s][0]) * CELL_SIZE), int((cellY + sight[s][1]) * CELL_SIZE),
                        int(CELL_SIZE), int(CELL_SIZE),
                        GL_LINE_LOOP, 0.3, 0.3, 0.3)

            drawEfCircle(int(c.xy.x + FIELD_X_OFFSET), int(c.xy.y), int(SIGHT_DISTANCE / 2), 30, GL_LINE_LOOP, 0.2, 0.2,
                         0.5)

        drawEfCircle(int(c.xy.x + FIELD_X_OFFSET), int(c.xy.y), int(CREATURE_SIZE * 1.4), 15, GL_POLYGON, 0.3, 0.3, 0.7)

    def drawTheChosenOneInfo(self):
        c = self.gameField.theChosenOne

        text(5, 80, "Direction (y axis inverted)", 1, 1, 1)
        text(20, 95, str(round(c.direction, 2)), 1, 1, 1)

        text(5, 115, "Food dist", 1, 1, 1)
        text(20, 130, str(round(c.debug_info[0], 2)), 1, 1, 1)

        text(5, 150, "Food dir (world, y axis inverted)", 1, 1, 1)
        text(20, 165, str(round(c.debug_info[1], 2)), 1, 1, 1)

        text(5, 185, "Food dir (relative, y axis inverted)", 1, 1, 1)
        text(20, 200, str(round((c.debug_info[1] - c.direction), 2)), 1, 1, 1)

        text(5, 220, "Fitness", 1, 1, 1)
        text(20, 235, str(round(c.fitness, 2)), 1, 1, 1)

        text(5, 255, "Speed", 1, 1, 1)
        text(20, 270, str(round(c.speed.length(), 2)), 1, 1, 1)

        x = 5
        for i in range(0, len(c.brain.neuronLayers)):
            y = 350
            for n in range(0, len(c.brain.neuronLayers[i][0])):
                text(x, y, str(round(c.brain.neuronLayers[i][0][n], 2)), 1, 1, 1)
                y += 15
            x += 35

    def drawCreatures(self):
        for i in range(0, len(self.gameField.creatures)):
            c = self.gameField.creatures[i]

            # creature
            drawEfCircle(FIELD_X_OFFSET + c.xy.x, c.xy.y, CREATURE_SIZE, 10, GL_POLYGON, 0,
                         c.fitness / STARTING_FITNESS, 0)
            # creature direction
            drawLine(int(FIELD_X_OFFSET + c.xy.x), int(c.xy.y),
                     int(FIELD_X_OFFSET + (c.xy.x + cos(c.direction) * CREATURE_SIZE)),
                     int((c.xy.y + sin(c.direction) * CREATURE_SIZE)), 1, 0.3, 0.3, 1)
            # creature's sight direction
            if not (c.debug_info[0] > 10000):  # inf
                drawLine(int(FIELD_X_OFFSET + c.xy.x), int(c.xy.y),
                         int(FIELD_X_OFFSET + (c.xy.x + cos(c.debug_info[1]) * c.debug_info[0])),
                         int((c.xy.y + sin(c.debug_info[1]) * c.debug_info[0])), 1, 1, 0.3, 0.3)

    def drawFood(self):
        for i in range(0, len(self.gameField.food)):
            drawEfCircle(FIELD_X_OFFSET + self.gameField.food[i].xy.x, self.gameField.food[i].xy.y, 2, 4, GL_POLYGON, 1,
                         1, 0.3)

    def drawGrid(self):
        r, g, b = 0.2, 0.28, 0.24
        for i in range(int(CELL_SIZE), int((FIELD_SIZE_X - CELL_SIZE) + CELL_SIZE), int(CELL_SIZE)):
            # vertical
            drawLine(i + FIELD_X_OFFSET, 0, i + FIELD_X_OFFSET, FIELD_SIZE_Y, 1, r, g, b)
            # horizontal
            drawLine(FIELD_X_OFFSET, i, X, i, 1, r, g, b)
