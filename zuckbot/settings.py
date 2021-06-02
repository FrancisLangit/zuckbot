import pygame


class Settings:
    """Settings of the application."""

    def __init__(self):
        """Initialize Settings class attributes."""

        # Screen 
        self.screen_size = (1200, 800)
        self.screen_background_color = (66, 103, 178)
        self.screen_caption = "Zuckbot"

        # Font
        self.font_color = (255, 255, 255)
        self.font_bold_filename = 'data/fonts/open_sans_bold.ttf'
        self.font_light_filename = 'data/fonts/open_sans_light.ttf'
        self.font_regular_filename = 'data/fonts/open_sans_reg.ttf'
        self.font_mono_filename = 'data/fonts/ibm_plex_mono_reg.ttf'

        # Question Input
        self.question_input_max_length = 64
        self.question_input_dest = (50, 50)

        # Zuckbot
        self.zuckbot_neutral_filename = ('data/images/zuckbot_neutral.jpg')