import sys
import pygame


class Main: 
    """Program's main class."""

    def __init__(self):
        """Initialize Main class attributes."""
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption('Zuckbot')


    def run(self):
        """Runs the game loop of the program."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()


if __name__ == '__main__':
    main = Main()
    main.run()