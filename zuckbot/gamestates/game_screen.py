import pygame

class Game_Screen:

    def __init__(self, main):
        """Initialize Game_Screen class attributes."""
        self.main = main
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.is_running = False


    def _check_keydown_events(self, event):
        """Checks of keydown events of the gamestate."""
        if event.key == pygame.K_ESCAPE:
            self.main.title_screen.is_running = True
            self.is_running = False
            

    def run_gamestate(self):
        """Runs the game loop of the gamestate."""
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

            pygame.display.flip()