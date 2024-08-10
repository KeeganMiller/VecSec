from pyray import *
from core.game_object import GameObject
from test_go import TestGo
from core.resource_manager import ResourceManager
from core.sprite import Sprite

class Main:

    _window_width: int = 1280
    _window_height: int = 720
    _window_title: str = "VecSec"
    full_screen: bool = False
    is_running: bool = True

    @staticmethod
    def create_window(**kwargs) -> None:
        if 'window_height' in kwargs and 'window_width' in kwargs:
            Main.window_width = kwargs['window_width']
            Main.window_height = kwargs['window_height']

        if 'fullscreen' in kwargs:
            Main.full_screen = kwargs['fullscreen']

        if 'window_title' in kwargs:
            Main._window_title = kwargs['window_title']

        init_window(Main._window_width, Main._window_height, Main._window_title)
        
    @staticmethod
    def create_resources():
        ResourceManager.load_texture(path="assets/test.png", name="test_sprite")
        spriteGo: Sprite = Sprite(name="sprite")
        spriteGo.set_texture(texture_name="test_sprite")
        ResourceManager.add_game_object(spriteGo)

    def run(**kwargs):
        set_target_fps(kwargs['fps'] if 'fps' in kwargs else 60)
        while Main.is_running and not window_should_close():
            # Update here
            ResourceManager._update(get_fps())

            begin_drawing()
            clear_background(WHITE)
            ResourceManager._draw()
            end_drawing()


Main.create_window()
Main.create_resources()
Main.run()