import glfw
import OpenGL

class EventListener:
    mouseX: int = -1
    mouseY: int = -1

    def keyCallback(self, window, key, scancode, action, mods):
        print(key, scancode, action)

    def mouseCallback(self, window, button, action, mods):
        print(button, action, (self.mouseX, self.mouseY))

    def cursorPositionCallback(self, window, xpos, ypos):
        self.mouseX = xpos
        self.mouseY = ypos
