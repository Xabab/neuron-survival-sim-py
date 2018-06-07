from src.engine.GameConstants import X, Y
from src.gui.Gui import drawGui
from src.render.GameField.GameFieldDrawer import drawGameField
from src.render.Shapes import *
from src.render.Text import text
from src.engine.EventsProcessing import *


def init():
    if not glfw.init():
        return

    _window = glfw.create_window(X, Y, "Fucking window", None, None)

    if not _window:
        glfw.terminate()

    glfw.make_context_current(_window)

    # SETTING UP WINDOW COORDINATE MATRIX #

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(0, X, Y, 0, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    eventListener = EventListener()
    glClearColor(1, 0, 1, 1.0)

    glfw.set_key_callback(_window, eventListener.keyCallback)
    glfw.set_mouse_button_callback(_window, eventListener.mouseCallback)
    glfw.set_cursor_pos_callback(_window, eventListener.cursorPositionCallback)

    #######################################




    while not glfw.window_should_close(_window):
        glClear(GL_COLOR_BUFFER_BIT)

        ##### RENDER HERE #####
        drawGui()

        drawGameField()

        #######################

        # print(glfw.get_cursor_pos(_window))

        # print(mouseX, mouseY)

        glfw.swap_buffers(_window)

        glfw.poll_events()


    glfw.terminate()


