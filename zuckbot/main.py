import pygame

from gamestates.title_screen import Title_Screen


class Main: 
    """Program's main class."""

    def __init__(self):
        """Initializes Main class attributes."""
        pygame.init()

        # Screen settings.
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Zuckbot')

        # Array of gamestates.
        self.gamestates = [
            Title_Screen(),
        ]


    def run_game(self):
        """Runs the game loop of the program."""
        for gamestate in self.gamestates:
            if gamestate.is_running:
                gamestate.run_gamestate()


if __name__ == '__main__':
    main = Main()
    main.run_game()