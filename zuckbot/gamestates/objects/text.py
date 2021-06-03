import pygame


class Text:
    """Object representing a text to be displayed."""

    def __init__(
        self, 
        gamestate, 
        font_filename, 
        font_size, 
        font_color,
        text, 
        rect_alignment=None, 
        x_offset=0, 
        y_offset=0):
        """Initialize Text class attributes.
        
        Parameters:
            gamestate (object)        : Gamestate where the object will be
                displayed.
            font_filename (string)    : Filename of the font.
            font_size (int)           : Size of the font.
            font_color (tuple)        : Color of font in (R, G, B) tuple.
            text (string)             : Text of the object.
            rect_alignment [optional] : Dict of kwargs to be passed into 
                get_rect().
            x_offset (int) [optional] : Pixels image will offset by on x-axis.
            y_offset (int) [optional] : Pixels image will offset by on y-axis. 
        """
        self.settings = gamestate.settings
        self.screen = gamestate.screen

        self.font_filename = font_filename
        self.font_size = font_size
        self.font_color = font_color
        self.text = text
        self.rect_alignment = rect_alignment
        self.x_offset = x_offset
        self.y_offset = y_offset

        self.image = self._get_image()
        self.image_rect = self._get_image_rect()


    def _get_image(self):
        """Returns an Pygame font image object made out of parameters."""
        font = pygame.font.Font(
            self.font_filename, 
            self.font_size,
        )
        font_image = font.render(
            self.text,
            True,
            self.font_color,
        )
        return font_image 


    def _get_image_rect(self):
        """Returns text image object's rect aligned and offset according to 
        parameters passed."""
        if (self.rect_alignment):
            image_rect = self.image.get_rect(**self.rect_alignment)
        else:
            image_rect = self.image.get_rect()
        image_rect.x += self.x_offset
        image_rect.y += self.y_offset
        return image_rect


    def blitme(self):
        """Blits the text objects onto the screen."""
        self.screen.blit(self.image, self.image_rect)


class Blinking_Text(Text):
    """Text with a feature allowing it to blink. Child of Text class."""

    def __init__(
        self, 
        gamestate, 
        font_filename, 
        font_size, 
        font_color,
        text, 
        rect_alignment=None, 
        x_offset=0, 
        y_offset=0):
        """Initialize Blinking_Text class attributes.
        
        Parameters:
            gamestate (object)        : Gamestate where the object will be
                displayed.
            font_filename (string)    : Filename of the font.
            font_size (int)           : Size of the font.
            font_color (tuple)        : Color of font in (R, G, B) tuple.
            text (string)             : Text of the object.
            rect_alignment [optional] : Dict of kwargs to be passed into 
                get_rect().
            x_offset (int) [optional] : Pixels image will offset by on x-axis.
            y_offset (int) [optional] : Pixels image will offset by on y-axis. 
        """
        super().__init__(gamestate, font_filename, font_size, font_color, 
            text, rect_alignment, x_offset, y_offset)
        self.blink_counter = 0
        
        
    def update_blink(self):
        """Checks blink counter of object and updates its text's appearance 
        based off of such."""
        self.blink_counter += 1
        if 0 < self.blink_counter < 150:
            self.font_color = self.settings.font_color
        elif 150 <= self.blink_counter < 300:
            self.font_color = self.settings.screen_background_color
        else:
            self.blink_counter = 0
        self.image = self._get_image()