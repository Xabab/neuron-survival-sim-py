from numpy import *

class Vector2d:

    def setVector(self, x: float, y: float):
        self.x = x
        self.y = y

    def add(self, v):
        self.x += v.x
        self.y += v.y

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @staticmethod
    def Vector2d(x: float, y: float):
        return Vector2d(x, y)


    @staticmethod
    def Vector2dCopy(c):
        return Vector2d(c.x, c.y)

    @staticmethod
    def Vector2dEqual(f: float):
        return Vector2d(f, f)

    def length(self):
        return sqrt(self.x*self.x + self.y*self.y)

