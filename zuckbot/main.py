import pygame

from gamestates.title_screen import Title_Screen
from gamestates.game_screen import Game_Screen
from settings import Settings


class Main: 
    """Program's main class."""

    def __init__(self):
        """Initializes Main class attributes."""
        pygame.init()

        self.settings = Settings()

        # Screen Configuration
        self.screen = pygame.display.set_mode(self.settings.screen_size)
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption(self.settings.screen_caption)

        # Gamestates
        self.title_screen = Title_Screen(self)
        self.game_screen = Game_Screen(self)
        self.gamestates = [self.title_screen, self.game_screen]


    def switch_gamestate(self, source_gamestate, target_gamestate):
        """Helper function used that shuts down source gamestate passed and 
        switches interface to target interface indicated."""
        source_gamestate.is_running = False
        target_gamestate.is_running = True
        target_gamestate.run_gamestate()


    def run_game(self):
        """Runs the game loop of the program."""
        for gamestate in self.gamestates:
            if gamestate.is_running:
                gamestate.run_gamestate()


if __name__ == '__main__':
    main = Main()
    main.run_game()