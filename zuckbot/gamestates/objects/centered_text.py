import pygame


class Centered_Text:
    """Centered text image object.
    
    Parameters:
        gamestate (object)        : Gamestate where the object will be displayed.
        font_filename (string)    : Filename of the font.
        font_size (int)           : Size of the font. 
        font_color (tuple)        : Color of the font in (R, G, B).    
        text (string)             : Text of the object.
        y_offset (int) [optional] : Pixels the image will offset by on y-axis. 
    """


    def __init__(self, gamestate, font_filename, font_size, font_color, text,
        y_offset=None):
            """Initialize object attributes."""
            self.gamestate = gamestate
            self.font_filename = font_filename
            self.font_size = font_size
            self.font_color = font_color
            self.text = text
            self.y_offset = y_offset

            self.image = self._get_image()
            self.image_rect = self._get_image_rect()


    def _get_image(self):
        """Returns a font image from parameter arguments."""
        font = pygame.font.Font(self.font_filename, self.font_size)
        image = font.render(
            self.text,
            True,
            self.font_color,
        )
        return image 


    def _get_image_rect(self):
        """Returns the rect of the font image offset by self.y_offset."""
        image_rect = self.image.get_rect(
            center=self.gamestate.screen_rect.center)
        if (self.y_offset):
            image_rect.y += self.y_offset
        return image_rect


    def blitme(self):
        """Blits the object onto the screen."""
        self.gamestate.screen.blit(self.image, self.image_rect)