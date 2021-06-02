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
            {'midtop': self.screen_rect.midtop},
            y_offset=20,
        )
        self.copyright_text = Text(
            self.gamestate, 
            self.settings.font_light_filename,
            14,
            self.settings.font_color,
            'Copyright © 2021 • francis.villanueva.langit@gmail.com',
            {'bottomleft': self.screen_rect.bottomleft},
            25,
            -20
        )
        self.stanford_text = Text(
            self.gamestate, 
            self.settings.font_light_filename,
            14,
            self.settings.font_color,
            'Stanford University • Code In Place 2021',
            {'bottomright': self.screen_rect.bottomright},
            -25,
            -20
        )
        

    def blitme(self):
        """Blits the object onto the screen."""
        self.esc_text.blitme()
        self.stanford_text.blitme()
        self.copyright_text.blitme()