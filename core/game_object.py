from pyray import *

class GameObject:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.position: Vector2 = Vector2(0, 0)
        self.scale: float = 1
        self.rotation: float = 0

    def _initialize(self):
        pass

    def _start(self):
        pass

    def _update(self):
        pass

    def _draw(self):
        pass

    def _destroy(self):
        pass

    