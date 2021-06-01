import random

import pygame
import pyttsx3


class Zuckbot:
    """Virtual reincarnation of Mark Zuckerberg."""


    def __init__(self, gamestate):
        """Initializes Zuckbot class attributes."""
        self.gamestate = gamestate
        self.settings = gamestate.settings
        self.screen = gamestate.screen
        self.screen_rect = gamestate.screen_rect

        self.tts_engine = pyttsx3.init()
        self.answers = self._get_answers_dict()

        self.image = pygame.image.load(self.settings.zuckbot_negative_filename)
        self.image_rect = self.image.get_rect(center=self.screen_rect.center)


    def _get_answers_dict(self):
        """Returns a dictionary of answer-image key-value pairs."""
        return {
            **dict.fromkeys(
                self.settings.zuckbot_affirmative_answers,
                pygame.image.load(self.settings.zuckbot_affirmative_filename)
            ),
            **dict.fromkeys(
                self.settings.zuckbot_noncomittal_answers,
                pygame.image.load(self.settings.zuckbot_noncomittal_filename)
            ),
            **dict.fromkeys(
                self.settings.zuckbot_negative_answers,
                pygame.image.load(self.settings.zuckbot_negative_filename)
            )
        }


    def _get_answer(self):
        """Returns a random key-value pair from answer dictionary in the form 
        of a tuple."""
        return random.choice(list(self.answers.items()))


    def answer(self):
        """Makes Zuckbot speak an answer and display an image from a randomly 
        chosen tuple value."""
        answer = self._get_answer()
        self.tts_engine.say(answer[0])
        self.tts_engine.runAndWait()


    def blitme(self):
        """Blits the object onto the screen."""
        self.screen.blit(self.image, self.image_rect)