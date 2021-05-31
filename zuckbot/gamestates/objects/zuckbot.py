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


    def speak(self):
        """Makes Zuckbot's text-to-speech engine say something random."""
        random_answer = random.choice(list(self.answers.items()))
        self.tts_engine.say(random_answer[0])
        self.tts_engine.runAndWait()