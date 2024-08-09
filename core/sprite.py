from pyray import *
from core.game_object import GameObject
from core.resource_manager import ResourceManager, TextureData

class Sprite(GameObject):
    def __init__(self, name: str, texture_name: str):
        super().__init__(name = name)
        self.texture_name: str = texture_name
        self.texture: TextureData

    def set_texture(self, **kwargs) -> None:
        if 'texture_name' in kwargs:
            self.texture = ResourceManager.get_texture(name=kwargs['texture_name'])
            if self.texture is None:
                print(f"Failed to load texture with name: {kwargs['texture_name']}")
            else:
                return
        elif 'texture_path' in kwargs:
            self.texture = ResourceManager.get_texture(path=kwargs['texture_path'])
            if self.texture is None:
                print(f"Failed to locate texture with path, attempting to load new texture...")
            else:
                return
            
        if 'texture_path' in kwargs:
            self.texture = ResourceManager.load_texture(kwargs['texture_path'])
            if self.texture is None:
                print(f'Failed to load texture with path {kwargs['texture_path']}')
            else:
                print(f'{self.texture.name} successfully loaded')
            
        
