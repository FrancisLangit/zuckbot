import random

import pygame

from .centered_text import Centered_Text
from .zuckbot_answers import Zuckbot_Answers


class Zuckbot:
    """Virtual reincarnation of Mark Zuckerberg."""


    def __init__(self, gamestate):
        """Initializes Zuckbot class attributes."""
        self.gamestate = gamestate
        self.settings = gamestate.settings
        self.screen = gamestate.screen
        self.screen_rect = gamestate.screen_rect

        self.answers = Zuckbot_Answers().get()

        self.answer_image = pygame.image.load(
            self.settings.zuckbot_neutral_filename)
        self.answer_image_rect = self._get_answer_image_rect()

        self.answer_text = self._get_answer_text('Awaiting input.')
        

    def _get_answer_image_rect(self):
        """Returns rect of Zuckbot's Pygame image object. To be used as pos 
        when blitting to screen."""
        answer_image_rect = self.answer_image.get_rect(
            center=self.screen_rect.center)
        answer_image_rect.y -= 10
        return answer_image_rect


    def _get_answer_text(self, answer_string):
        """Returns Centered_Text instance with text set to answer_string."""
        return Centered_Text(
            self.gamestate, 
            self.settings.font_mono_filename,
            25,
            self.settings.font_color,
            answer_string,
            250,
        )


    def answer(self):
        """Makes Zuckbot speak a randomly chosen answer and change appearance 
        in accordance with such."""
        answer = random.choice(self.answers)
        answer['sound'].play()
        self.answer_image = answer['image']
        self.answer_text = self._get_answer_text(answer['text'])


    def reset(self):
        """Resets Zuckbot's text and image back to default values."""
        self.answer_text = self._get_answer_text('Awaiting input.')
        self.answer_image = pygame.image.load(
            self.settings.zuckbot_neutral_filename)

    
    def update(self):
        """Checks if Zuckbot is already answering. If not, calls reser()."""
        if not pygame.mixer.get_busy():
            self.reset()


    def blitme(self):
        """Blits the object onto the screen."""
        self.screen.blit(self.answer_image, self.answer_image_rect)
        self.answer_text.blitme()