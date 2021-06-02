from .text import Text

class Footer:


    def __init__(self, gamestate):
        self.gamestate = gamestate
        self.settings = gamestate.settings
        self.screen = gamestate.screen
        self.screen_rect = gamestate.screen_rect

        self.copyright_text = Text(
            self.gamestate, 
            self.settings.font_light_filename,
            14,
            self.settings.font_color,
            'MIT License • Copyright © 2021 • Francis Langit',
            {'bottomleft': self.screen_rect.bottomleft},
            25,
            -20
        )
        self.email_text = Text(
            self.gamestate, 
            self.settings.font_light_filename,
            14,
            self.settings.font_color,
            'francis.villanueva.langit@gmail.com',
            {'bottomright': self.screen_rect.bottomright},
            -25,
            -20
        )


    def blitme(self):
        self.copyright_text.blitme()
        self.email_text.blitme()