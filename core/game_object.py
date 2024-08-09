from __future__ import annotations
from pyray import *


class GameObject:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.local_position: Vector2 = Vector2(0, 0)
        self.local_scale: Vector2 = Vector2(0, 0)
        self.rotation: float = 0

        self.parent: GameObject = None
        self.children: list[GameObject] = []

        self.is_active: bool = True

    def _initialize(self):
        pass

    def _start(self):
        pass

    def _update(self, dt: float):
        pass

    def _draw(self):
        pass

    def _destroy(self):
        pass

    
    @property
    def parent(self):
        return self.parent
    
    @parent.setter
    def parent(self, value: GameObject):
        if not parent == None:
            self.parent.children.remove(self)

        parent = value
        if not parent == None:
            self.parent.children.add(self)


    @property
    def position(self):
        if not self.parent == None:
            return self.local_position
        else:
            return vector2_add(self.parent.position, self.local_position)
        
    @position.setter
    def position(self, value: Vector2):
        self.local_position = value

    @property
    def rotation(self):
        if not self.parent == None:
            return self.local_rotation
        else:
            return self.parent.rotation + self.local_rotation
        
    @rotation.setter
    def rotation(self, value: float):
        self.local_rotation = value

    @property
    def scale(self):
        if not self.parent == None:
            return self.local_scale
        else:
            return vector2_multiply(self.parent.scale, self.local_scale)
        

    @scale.setter
    def scale(self, value: float):
        self.local_scale = value


    