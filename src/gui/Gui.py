from time import time as t

from src.gui.Button import Button
from src.logic import Game
from src.render.Text import text

g = Game.g
_time: int = None
_fps: int = 0
_counter: int = 0

class ButtonDecSpeed(Button):
    def onClick(self):
        Game.g.iterationCount_mm()
        print("counting " + str(Game.Game.desiredIterationCount) + " iterations per frame")



class ButtonIncSpeed(Button):
    def onClick(self):
        Game.g.iterationCount_pp()
        print("counting " + str(Game.Game.desiredIterationCount) + " iterations per frame")


buttons = [ButtonDecSpeed(10, 15, 30, 30, 0, 0, 0, "<<"), ButtonIncSpeed(50, 15, 30, 30, 0, 0, 0, ">>")]


def drawButtons():
    for i in range(0, buttons.__len__()):
        buttons[i].drawButton()


def drawGui(time=[_time], fps=[_fps], counter=[_counter]):
    drawButtons()

    if time[0] is None:
        time[0] = int(t())

    tmp = int(t())

    if tmp > time[0]:
        time[0] = tmp
        fps[0] = counter[0]
        counter[0] = 0
    else:
        counter[0] += 1

    text(0, 10, "fps: " + str(fps[0]) + " iterations: " + str(fps[0] * g.desiredIterationCount), 1, 1, 1)
