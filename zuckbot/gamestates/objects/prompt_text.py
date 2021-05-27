import pygame


class Prompt_Text:
    """Text prompting the user to hit enter key to exit the title screen."""

    def __init__(self, gamestate):
        """Initializes Title_Text class attributes."""
        self.gamestate = gamestate
        self.settings = gamestate.settings
        
        self.font = pygame.font.Font(self.settings.font_light_filename, 48)
        self.image = self.font.render(
            "Press Enter", 
            True, 
            self.settings.font_color, 
        )
        self.image_rect = self.image.get_rect(
            center=self.gamestate.screen_rect.center)
        self.image_rect.y += 75

    def blitme(self):
        """Blits the object onto the screen."""
        self.gamestate.screen.blit(self.image, self.image_rect)