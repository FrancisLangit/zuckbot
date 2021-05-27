import pygame


class Title_Text: 
    """Text displaying title of game on title screen gamestate."""

    def __init__(self, gamestate):
        """Initializes Title_Text class attributes."""
        self.gamestate = gamestate
        self.font = pygame.font.SysFont(None, 48)
        self.image = self.font.render(
            "Zuckbot", 
            True, 
            (255, 255, 255), 
            (0, 0, 0)
        )
        self.image_rect = self.image.get_rect(
            center=self.gamestate.screen_rect.center)

    def blitme(self):
        """Blits the object onto the screen."""
        self.gamestate.screen.blit(self.image, self.image_rect)
        
        

class Title_Screen:
    """Title screen gamestate."""

    def __init__(self, main):
        """Initializes Title_Screen class attributes."""
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.title_text = Title_Text(self)

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

            self.title_text.blitme()

            pygame.display.flip()