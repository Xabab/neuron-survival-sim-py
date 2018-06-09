from src.engine.GameConstants import *
from src.gui.Button import Button
from src.logic import Game
from src.render.Shapes import drawBox

g = Game.g

class ButtonDecSpeed(Button):
    def onClick(self):
        Game.g.iterationCount_mm()
        print("counting " + str(Game.Game.desiredIterationCount) + " iterations per frame")



class ButtonIncSpeed(Button):
    def onClick(self):
        Game.g.iterationCount_pp()
        print("counting " + str(Game.Game.desiredIterationCount) + " iterations per frame")


buttons = [ButtonDecSpeed(10, 10, 30, 30, 0, 0, 0, "<<"),  ButtonIncSpeed(50, 10, 30, 30, 0, 0, 0, ">>")]


def drawButtons():
    for i in range(0, buttons.__len__()):
        buttons[i].drawButton()


def drawGui():
    drawBox(0, 0, X, Y, 0.2, 0.25, 0.2)
    drawBox(0, 0, MENU_WIDTH, Y, 0.4, 0.4, 0.43)
    drawButtons()

