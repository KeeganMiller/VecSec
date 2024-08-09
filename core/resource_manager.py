from pyray import *
from game_object import *

class ResourceManager:
    objects_to_start: list[GameObject] = []
    active_objects: list[GameObject] = []

    @staticmethod
    def add_game_object(go: GameObject):
        if go not in ResourceManager.active_objects and go not in ResourceManager.objects_to_start:
            go._initialize()
            ResourceManager.objects_to_start.append(go)

    @staticmethod
    def remove_game_object(go: GameObject):
        if go in ResourceManager.objects_to_start:
            ResourceManager.objects_to_start.remove(go)
        elif go in ResourceManager.active_objects:
            ResourceManager.active_objects.remove(go)

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
