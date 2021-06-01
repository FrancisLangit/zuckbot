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

        # Zuckbot Answers
        self.zuckbot_affirmative_answers = [
            "I don't see why that isn't possible.",
            "It's almost a disadvantage if you're not on it now",
            'Sure, if you do the things that are easier first.',
            "There's a lot of that in Silicon Valley",
            'Yes.',
            "Yes, I believe that that's correct.",
        ]
        self.zuckbot_noncomittal_answers = [
            "Can't really give you an answer to that one."
            "I don't know the answer to that off the top of my head.",
            'I hope not.',
            "I'm not sure what that means.",
            "I'm not sure of the answer to that question.",
            'Maybe.',
            'This is a complex issue that deserves more than one word.',
        ]
        self.zuckbot_negative_answers = [
            'A squirrel dying in front of your house may be more relevant.',
            "Certainly doesn't feel like that to me.",
            'I think that is somewhat of a burden.',
            "No.",
            "No, I would not choose to do that publicly here.",
        ]

        # Zuckbot Images
        self.zuckbot_neutral_filename = (
            'data/images/zuckbot_neutral.jpg')
        self.zuckbot_affirmative_filename = (
            'data/images/zuckbot_affirmative.jpg')
        self.zuckbot_noncomittal_filename = (
            'data/images/zuckbot_noncomittal.jpg')
        self.zuckbot_negative_filename = (
            'data/images/zuckbot_negative.jpg')