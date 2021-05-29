import sys
sys.path.append(".") 

import pygame

from .objects.centered_text import Centered_Text


class Title_Screen:
    """Title screen gamestate."""

    def __init__(self, main):
        """Initializes Title_Screen class attributes."""
        self.main = main
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.title_text = Centered_Text(
            self,
            self.settings.font_bold_filename,
            96,
            self.settings.font_color,
            "zuckbot",
            -50,
        )
        self.prompt_text = Centered_Text(
            self,
            self.settings.font_light_filename,
            48,
            self.settings.font_color,
            "Press Enter",
            50,
        )
        
        self.is_running = True


    def _check_keydown_events(self, event):
        """Checks of keydown events of the gamestate."""
        if event.key == pygame.K_ESCAPE:
            sys.exit()
        if event.key == pygame.K_RETURN:
            self.is_running = False
            self.main.game_screen.is_running = True


    def run_gamestate(self):
        """Runs the game loop of the gamestate."""
        while self.is_running:
            self.screen.fill(self.settings.screen_background_color)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

            self.title_text.blitme()
            self.prompt_text.blitme()

            pygame.display.flip()