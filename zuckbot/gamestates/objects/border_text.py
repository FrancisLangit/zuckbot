from .text import Text


class Border_Text:
    """Text found along borders of Game Screen gamestate."""


    def __init__(self, gamestate):
        """Initialize Border_Text class attributes.
        
        Parameters:
            gamestate (object) : Gamestate object where text will be 
                displayed in.
        """
        self.gamestate = gamestate
        self.settings = gamestate.settings
        self.screen = gamestate.screen
        self.screen_rect = gamestate.screen_rect

        self.esc_text = Text(
            self.gamestate,
            self.settings.font_light_filename,
            14,
            self.settings.font_color,
            'Press ESC to exit to title screen.',
            {'topleft': self.screen_rect.topleft},
            25,
            20
        )
        self.stanford_text = Text(
            self.gamestate,
            self.settings.font_light_filename,
            14,
            self.settings.font_color,
            'Stanford University • Code In Place 2021',
            {'topright': self.screen_rect.topright},
            -25,
            20
        )
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
        """Blits the object onto the screen."""
        self.esc_text.blitme()
        self.stanford_text.blitme()
        self.copyright_text.blitme()
        self.email_text.blitme()