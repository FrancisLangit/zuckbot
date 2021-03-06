import sys
sys.path.append(".") 

import pygame

from .objects.text import Text, Blinking_Text


class Title_Screen:
    """Title screen gamestate."""

    def __init__(self, main):
        """Initializes Title_Screen class attributes."""
        self.main = main
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.title_text = self._get_title_text()
        self.prompt_text = self._get_prompt_text()
        self.prompt_text_blink_count = 0
        
        self.is_running = True


    def _get_title_text(self):
        """Returns Text instance representing title text."""
        return Text(
            self,
            self.settings.font_bold_filename,
            96,
            self.settings.font_color,
            'zuckbot',
            {'center': self.screen_rect.center},
            0,
            -50,
        )


    def _get_prompt_text(self):
        """Returns Text instance prompting user to press enter."""
        return Blinking_Text(
            self,
            self.settings.font_light_filename,
            48,
            self.settings.font_color,
            'Press Enter',
            {'center': self.screen_rect.center},
            0,
            50,
        )


    def _check_keydown_events(self, event):
        """Checks keydown events of the gamestate."""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_RETURN:
            self.main.switch_gamestate(self, self.main.game_screen)


    def _check_events(self):
        """Checks events of the gamestate."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)


    def run_gamestate(self):
        """Runs the game loop of the gamestate."""
        while self.is_running:
            self.screen.fill(self.settings.screen_background_color)

            self._check_events()

            self.prompt_text.update_blink()

            self.title_text.blitme()
            self.prompt_text.blitme()

            pygame.display.flip()