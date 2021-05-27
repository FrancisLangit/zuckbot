import pygame


class Title_Text: 
    """Text displaying title of game on title screen gamestate."""

    def __init__(self, gamestate):
        """Initializes Title_Text class attributes."""
        self.gamestate = gamestate
        self.font = pygame.font.SysFont(None, 96)
        self.image = self.font.render(
            "Zuckbot", 
            True, 
            (255, 255, 255), 
            (0, 0, 0)
        )
        self.image_rect = self.image.get_rect(
            center=self.gamestate.screen_rect.center)
        self.image_rect.y -= 100

    def blitme(self):
        """Blits the object onto the screen."""
        self.gamestate.screen.blit(self.image, self.image_rect)
