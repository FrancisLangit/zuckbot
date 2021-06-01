import random
import threading

import pygame
import pyttsx3

from .centered_text import Centered_Text


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

        self.answer_image = pygame.image.load(
            self.settings.zuckbot_neutral_filename)
        self.answer_image_rect = self.answer_image.get_rect(
            center=self.screen_rect.center)
        self.answer_image_rect.y -= 10

        self.answer_text = self._get_answer_text('Awaiting input.')


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


    def _update_visuals(self, answer_image, answer_string):
        """Updates the answer image and answer text of Zuckbot."""
        self.answer_image = answer_image
        self.answer_text = self._get_answer_text(answer_string)

    
    def _say_answer(self, answer_string):
        """Makes text-to-speech engine of Zuckbot say answer string passed. 
        Text to speech engine is run on a separate thread.
        
        Arguments:
            answer_string (str) : String for TTS engine to say."""
        self.tts_engine.say(answer_string)
        threading.Thread(target=self.tts_engine.runAndWait).start()


    def answer(self):
        """Makes Zuckbot speak an answer and display an image from a randomly 
        chosen tuple value."""
        answer = self._get_answer()
        self._update_visuals(answer[1], answer[0])
        self._say_answer(answer[0])


    def blitme(self):
        """Blits the object onto the screen."""
        self.screen.blit(self.answer_image, self.answer_image_rect)
        self.answer_text.blitme()