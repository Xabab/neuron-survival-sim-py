from src.engine.EventsProcessing import *
from src.render.Shapes import *
from src.render.Text import *



class Button:
    _cR: float
    _cG: float
    _cB: float
    _sizeX: int
    _sizeY: int
    _posX: int
    _posY: int
    _title: str

    def __init__(self, posX: int, posY: int, sizeX: int, sizeY: int, cR: float, cG: float, cB: float, title: str):
        self._cR = cR
        self._cG = cG
        self._cB = cB
        self._sizeX = sizeX
        self._sizeY = sizeY
        self._posX = posX
        self._posY = posY
        self._title = title

    def checkForClick(self):
        if ((mouseX > self._posX) & (mouseX < (self._posX + self._sizeX)) &
                (mouseY > self._posY) & (mouseY < (self._posY + self._sizeY))):
            self.onClick()

    def onClick(self):
        raise NotImplemented("Define onClick() function in a child class!")

    def drawButton(self):
        drawBox(self._posX, self._posY, self._sizeX, self._sizeY, self._cR, self._cG, self._cB)

        text(self._posX + 9, self._posY + 16, self._title, 1, 1, 1)