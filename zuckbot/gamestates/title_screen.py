import pygame


class Title_Screen:
    """Title screen gamestate."""

    def __init__(self):
        """Initializes Title_Screen class attributes."""
        self.is_running = True

    def _check_keydown_events(self, event):
        """Checks of keydown events of the gamestate."""
        if event.key == pygame.K_RETURN:
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