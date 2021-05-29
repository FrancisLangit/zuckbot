import pygame

class Settings:
    """"""

    def __init__(self):
        """Initialize Settings class attributes."""

        # Screen 
        self.screen_size = (1200, 800)
        self.screen_background_color = (66, 103, 178)
        self.screen_caption = "Zuckbot"

        # Font
        self.font_color = (255, 255, 255)
        self.font_bold_filename = './zuckbot/data/Open Sans Bold.ttf'
        self.font_light_filename = './zuckbot/data/Open Sans Light.ttf'
        self.font_regular_filename = './zuckbot/data/Open Sans Regular.ttf'