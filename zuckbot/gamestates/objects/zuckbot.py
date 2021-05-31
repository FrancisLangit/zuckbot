import random

import pyttsx3


class Zuckbot:
    """Virtual reincarnation of Mark Zuckerberg."""


    def __init__(self):
        """Initializes Zuckbot class attributes."""
        self.tts_engine = pyttsx3.init()

        self.answers = [
            # Affirmative
            """Yes, I believe that that's correct.""",
            """If you do the things that are easier first, then you can 
            actually make a lot of progress.""",
            """It's almost a disadvantage if you're not on it now.""",
            """There's a lot of that in Silicon Valley.""",
            """Yes.""",

            # Non-commital
            """I'm not sure what that means.""",
            """I'm not sure of the answer to that question.""",
            """I hope not.""",
            """This is a complex issue that I think deserves more than a one 
            word answer.""",
            """I don't know the answer to that off the top of my head.""",

            # Negative
            """A squirrel dying in front of your house may be more relevant to
            your interests right now.""",
            """Certainly doesn't feel like that to me.""",
            """No, I would not choose to do that publicly here.""",
            """If you're always under the pressure of real identity, I think 
            that is somewhat of a burden.""",        
            """No.""",
        ]


    def speak(self):
        """Makes Zuckbot's text-to-speech engine say something random."""
        self.tts_engine.say(random.choice(self.answers))
        self.tts_engine.runAndWait()