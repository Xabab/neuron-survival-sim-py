from src.render.Shapes import *
from src.render.Text import *



class Button:
    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int, cR: float, cG: float, cB: float, title: str):
        self._cR = cR
        self._cG = cG
        self._cB = cB
        self._sizeX = sizeX
        self._sizeY = sizeY
        self._posX = posX
        self._posY = posY
        self._title = title

    def checkForClick(self, x: int, y: int):
        print("click check")
        if ((x > self._posX) & (x < (self._posX + self._sizeX)) &
                (y > self._posY) & (y < (self._posY + self._sizeY))):
            self.onClick()

    def onClick(self):
        raise NotImplemented("Define onClick() function in a child class!")

    def drawButton(self):
        drawBox(self._posX, self._posY, self._sizeX, self._sizeY, self._cR, self._cG, self._cB)

        text(self._posX + 9, self._posY + 16, self._title, 1, 1, 1)