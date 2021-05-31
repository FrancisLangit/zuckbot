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
        self.font_bold_filename = './zuckbot/data/fonts/open_sans_bold.ttf'
        self.font_light_filename = './zuckbot/data/fonts/open_sans_light.ttf'
        self.font_regular_filename = './zuckbot/data/fonts/open_sans_reg.ttf'

        # Question Input
        self.question_input_max_length = 64
        self.question_input_dest = (50, 50)

        # Zuckbot
        self.zuckbot_neutral_filename = (
            './zuckbot/data/images/zuckbot_neutral.jpg')
        self.zuckbot_affirmative_filename = (
            './zuckbot/data/images/zuckbot_affirmative.jpg')
        self.zuckbot_noncomittal_filename = (
            './zuckbot/data/images/zuckbot_noncomittal.jpg')
        self.zuckbot_negative_filename = (
            './zuckbot/data/images/zuckbot_negative.jpg')