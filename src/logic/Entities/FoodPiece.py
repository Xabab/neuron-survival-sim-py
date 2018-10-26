from logic import Vector2d


class FoodPiece:

    def __init__(self, x: float, y: float):
        self.xy = Vector2d.Vector2d(x, y)
