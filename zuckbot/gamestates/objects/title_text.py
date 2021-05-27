import pygame


class Title_Text: 
    """Text displaying title of game on title screen gamestate."""

    def __init__(self, gamestate):
        """Initializes Title_Text class attributes."""
        self.gamestate = gamestate
        self.settings = gamestate.settings

        self.font = pygame.font.Font(self.settings.font_bold_filename, 96)
        self.image = self.font.render(
            "zuckbot", 
            True, 
            self.settings.font_color, 
        )
        self.image_rect = self.image.get_rect(
            center=self.gamestate.screen_rect.center)
        self.image_rect.y -= 50

    def blitme(self):
        """Blits the object onto the screen."""
        self.gamestate.screen.blit(self.image, self.image_rect)
