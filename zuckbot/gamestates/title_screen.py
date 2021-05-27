import sys
sys.path.append(".") 

import pygame

from .objects.title_text import Title_Text
from .objects.prompt_text import Prompt_Text


class Title_Screen:
    """Title screen gamestate."""

    def __init__(self, main):
        """Initializes Title_Screen class attributes."""
        self.main = main
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.title_text = Title_Text(self)
        self.prompt_text = Prompt_Text(self)

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