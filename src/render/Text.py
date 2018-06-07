from OpenGL.GLUT import *
from OpenGL.GL import *

from src.engine.GameConstants import Y


def text(x: int, y: int, text: str, cR: float, cG: float, cB: float):
    if glutInit():
        return

    glColor3f(cR, cG, cB)
    glWindowPos2f(x, Y - y)

    ch = 0

    while ch < len(text):
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_10, ctypes.c_int(ord(text[ch])))
        ch += 1


