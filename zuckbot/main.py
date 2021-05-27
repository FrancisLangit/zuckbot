import pygame

from gamestates.title_screen import Title_Screen
from gamestates.game_screen import Game_Screen


class Main: 
    """Program's main class."""

    def __init__(self):
        """Initializes Main class attributes."""
        pygame.init()

        # Screen Settings
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption('Zuckbot')

        # Gamestates
        self.title_screen = Title_Screen(self)
        self.game_screen = Game_Screen(self)

        self.gamestates = [
            self.title_screen,
            self.game_screen,
        ]


    def run_game(self):
        """Runs the game loop of the program."""
        for gamestate in self.gamestates:
            if gamestate.is_running:
                gamestate.run_gamestate()


if __name__ == '__main__':
    main = Main()
    main.run_game()