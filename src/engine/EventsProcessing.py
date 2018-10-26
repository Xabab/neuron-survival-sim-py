from engine.GameConstants import MENU_WIDTH
from gui import Gui
from logic import Game


class EventListener:
    mouseX: int = -1
    mouseY: int = -1

    def keyCallback(self, window, key, scancode, action, mods):
        # print(key, scancode, action)

        pass

    def mouseCallback(self, window, button, action, mods):
        # print(button, action, (self.mouseX, self.mouseY))

        # print("mouse ping")

        if (button == 0) & (action == 1):
            if self.mouseX > MENU_WIDTH:
                # print("mouse pong 1")
                Game.g.choseCreature(self.mouseX, self.mouseY)
            else:
                for b in Gui.buttons[:]:
                    # print("mouse pong 2")
                    b.checkForClick(self.mouseX, self.mouseY)

    def cursorPositionCallback(self, window, xpos, ypos):
        self.mouseX = xpos
        self.mouseY = ypos
