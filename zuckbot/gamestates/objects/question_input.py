import pygame

from .pygame_textinput import TextInput


class Question_Input:
    """Input field where user enters what they'd like to ask Zuckbot."""


    def __init__(self, gamestate):
        """Initialize Question_Input class attributes."""
        self.settings = gamestate.settings
        self.screen = gamestate.screen
        self.text_input = self._get_text_input()
        self.bottom_border_rect = pygame.Rect(50, 105, 1100, 1)


    def _get_text_input(self):
        """Returns a pygame_textinput.TextInput object acting as text field of 
        the object."""
        return TextInput(
            initial_string="> ",
            font_family=self.settings.font_regular_filename,
            antialias=True,
            text_color=self.settings.font_color,
            cursor_color=self.settings.font_color,
            max_string_length=self.settings.question_input_max_length,
        )


    def update(self, events):
        """Updates the contents of the object's text input."""
        self.text_input.update(events)


    def blitme(self):
        """Blits the object onto the screen."""
        self.screen.blit(
            self.text_input.get_surface(),
            self.settings.question_input_dest,
        )
        pygame.draw.rect(
            self.screen, 
            self.settings.font_color, 
            self.bottom_border_rect
        )