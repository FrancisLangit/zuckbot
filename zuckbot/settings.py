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
            "Yes, I believe that that's correct",
            ('If you do the things that are easier first, then you can '
             'actually make a lot of progress.'),
            "It's almost a disadvantage if you're not on it now",
            "There's a lot of that in Silicon Valley",
            "I don't see why that isn't possible."
            'Yes.',
        ]
        self.zuckbot_noncomittal_answers = [
            "I'm not sure what that means.",
            "I'm not sure of the answer to that question.",
            'I hope not.',
            ('This is a complex issue that I think deserves more than a '
             'one word answer.'),
            "I don't know the answer to that off the top of my head.",
            'Maybe.',
            "Can't really give you an answer to that one."
        ]
        self.zuckbot_negative_answers = [
            ('A squirrel dying in front of your house may be more relevant '
             'to your interests right now.'),
            "Certainly doesn't feel like that to me.",
            "No, I would not choose to do that publicly here.",
            ("If you're always under the pressure of real identity, I think "
             "that is somewhat of a burden."),
            "No.",
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