from pyray import *

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
        

    def run(**kwargs):
        set_target_fps(kwargs['fps'] if 'fps' in kwargs else 60)
        while Main.is_running and not window_should_close():
            # Update here
            print('Hello, World!')

            begin_drawing()
            clear_background(WHITE)
            draw_text("Hello, World", 100, 100, 32, BLACK)
            end_drawing()


Main.create_window()
Main.run()