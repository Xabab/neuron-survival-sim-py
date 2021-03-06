from OpenGL.GL import *
from numpy import *


def drawCircle(center_x: int, center_y: int, radius: int, count_of_polygons: int, mode, cR: float, cG: float, cB: float,
               cA: float = 1.):
    glColor4f(cR, cG, cB, cA)
    glLineWidth(1)
    glBegin(mode)
    for i in range(0, count_of_polygons):
        glVertex2d((center_x + sin(((2 * pi) / count_of_polygons) * i) * radius),
                   (center_y + cos(((2 * pi) / count_of_polygons) * i) * radius))

    glEnd()


def drawEfCircle(center_x: int, center_y: int, radius: int, count_of_polygons: int, mode, cR: float, cG: float,
                 cB: float, cA: float = 1.):
    # circle w/o sin/cos functions. (c) http://slabode.exofire.net/circle_draw.shtml
    glColor4f(cR, cG, cB, cA)

    theta = 2 * pi / count_of_polygons
    tangential_factor = tan(theta)
    radial_factor = cos(theta)

    x = radius
    y = 0

    glBegin(mode)

    for i in range(0, count_of_polygons):

        glVertex2f(x + center_x, y + center_y)

        tx = -y
        ty = x

        x += tx * tangential_factor
        y += ty * tangential_factor

        x *= radial_factor
        y *= radial_factor

    glEnd()


def drawBox(x: int, y: int, size_x: int, size_y: int, mode, cR: float, cG: float, cB: float, cA: float = 1.):
    glColor4f(cR, cG, cB, cA)
    glLineWidth(1)
    glBegin(mode)

    glVertex2i(x, y)
    glVertex2i(x, y + size_y)
    glVertex2i(x + size_x, y + size_y)
    glVertex2i(x + size_x, y)

    glEnd()


def drawLine(x1: int, y1: int, x2: int, y2: int, width: int, cR: float, cG: float, cB: float, cA: float = 1.):
    glColor4f(cR, cG, cB, cA)
    glLineWidth(width)

    glBegin(GL_LINES)

    glVertex2i(x1, y1)
    glVertex2i(x2, y2)

    glEnd()
