from pyray import *
from game_object import *

class ResourceManager:
    objects_to_start: list[GameObject] = []
    active_objects: list[GameObject] = []

    @staticmethod
    def _update(dt: float):
        for obj in ResourceManager.active_objects:
            if obj.is_active:
                obj._update(dt)

        for obj in ResourceManager.objects_to_start:
            if obj.is_active:
                obj._start()
                ResourceManager.active_objects.append(obj)
                ResourceManager.objects_to_start.remove(obj)

    @staticmethod
    def _draw():
        for obj in ResourceManager.active_objects:
            if obj.is_active:
                obj._draw()
