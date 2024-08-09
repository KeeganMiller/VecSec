from pyray import *
from core.game_object import GameObject

class TestGo(GameObject):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def _update(self, dt: float) -> None:
        super()._update(dt)
        print("GO:", self.name)

    def _draw(self) -> None:
        super()._draw()
        draw_text(f"GO: {self.name}", int(self.position.x), int(self.position.y), 32, BLACK)
