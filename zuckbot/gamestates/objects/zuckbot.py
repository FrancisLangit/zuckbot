import random

import pygame
import pyttsx3

import pprint

class Zuckbot:
    """Virtual reincarnation of Mark Zuckerberg."""


    def __init__(self, gamestate):
        """Initializes Zuckbot class attributes."""
        self.gamestate = gamestate
        self.settings = gamestate.settings
        self.screen = gamestate.screen
        self.screen_rect = gamestate.screen_rect

        self.tts_engine = pyttsx3.init()

        self.affirmative_answers = dict.fromkeys(
            [
                """Yes, I believe that that's correct.""",
                """If you do the things that are easier first, then you can 
                    actually make a lot of progress.""",
                """It's almost a disadvantage if you're not on it now.""",
                """There's a lot of that in Silicon Valley.""",
                """Yes.""",
            ], 
            pygame.image.load(self.settings.zuckbot_affirmative_filename)
        )

        self.noncommital_answers = dict.fromkeys(
            [
                """I'm not sure what that means.""",
                """I'm not sure of the answer to that question.""",
                """I hope not.""",
                """This is a complex issue that I think deserves more than a 
                    one word answer.""",
                """I don't know the answer to that off the top of my head.""",
            ], 
            pygame.image.load(self.settings.zuckbot_noncomittal_filename)
        )

        self.negative_answers = dict.fromkeys(
            [
                """A squirrel dying in front of your house may be more 
                    relevant to your interests right now.""",
                """Certainly doesn't feel like that to me.""",
                """No, I would not choose to do that publicly here.""",
                """If you're always under the pressure of real identity, I 
                    think that is somewhat of a burden.""",        
                """No.""",
            ], 
            pygame.image.load(self.settings.zuckbot_negative_filename)
        )

        self.answers = {
            **self.affirmative_answers, 
            **self.noncommital_answers, 
            **self.negative_answers,
        }

    def speak(self):
        """Makes Zuckbot's text-to-speech engine say something random."""
        random_answer = random.choice(list(self.answers.items()))

        self.tts_engine.say(random_answer[0])
        self.tts_engine.runAndWait()