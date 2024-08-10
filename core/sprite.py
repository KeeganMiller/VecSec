from pyray import *
from core.game_object import GameObject
from core.resource_manager import ResourceManager, TextureData

class Sprite(GameObject):
    def __init__(self, name: str, **kwargs):
        super().__init__(name = name)
        self.texture_name: str = kwargs['texture_name'] if 'texture_name' in kwargs else ""
        self.texture: TextureData
        self.color = kwargs['tint'] if 'tint' in kwargs else WHITE
        self._source_rect: Rectangle = Rectangle(0, 0, 0, 0)
        self._dest_rect: Rectangle = Rectangle(0, 0, 0, 0)
        self._frame_size: Vector2 = Vector2(0, 0)
        self.origin: Vector2 = Vector2(0, 0)

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

    def set_frame_size(self, sizeX: int, sizeY: int):
        self._frame_size = Vector2(sizeX, sizeY)
        self._source_rect = Rectangle(self._source_rect.x, self._source_rect.y, sizeX, sizeY)

    def set_frame_position(self, framePosX: int, framePosY: int):
        self._source_rect = Rectangle(framePosX, framePosY, self._source_rect.width, self._source_rect.height)

    def _update(self, dt: float):
        super()._update(dt)
        if self._frame_size.x == 0 and self._frame_size.y == 0:
            self.set_frame_size(self.texture.texture.width, self.texture.texture.height)

        self._dest_rect = Rectangle(self.position.x, self.position.y, self._frame_size.x * self.scale.x, self._frame_size.y * self.scale.y)

    def _draw(self, **kwargs):
        super()._draw()
        if self.texture is not None and self.texture.texture.id > 0:
            draw_texture_pro(self.texture.texture, self._source_rect, self._dest_rect, self.origin, self.rotation, self.color)            
        
