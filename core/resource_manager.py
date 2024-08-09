from __future__ import annotations
from pyray import *
from core.game_object import *

class ResourceManager:
    objects_to_start: list[GameObject] = []
    active_objects: list[GameObject] = []

    loaded_textures: list[TextureData] = []

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

    @staticmethod
    def load_texture(path: str, name: str) -> TextureData | None:
        texture: Texture = load_texture(path)
        if texture.id > 0:
            data = TextureData(texture_name=name, texture_path=path, texture=texture)
            ResourceManager.loaded_textures.append(data)
            return data
        
    @staticmethod
    def get_texture(path: str = "", name: str = ""):
        return next((tex for tex in ResourceManager.loaded_textures if tex.texture_name == name or tex.path == path), None)
    
    @staticmethod
    def unload_texture_by_name(name: str):
        texture = ResourceManager.get_texture(name=name)
        if texture is not None:
            unload_texture(texture.texture)
    


class TextureData:
    def __init__(self, texture_name: str, texture_path: str, texture: Texture):
        self.texture_name = texture_name
        self.texture_path = texture_path
        self.texture = texture