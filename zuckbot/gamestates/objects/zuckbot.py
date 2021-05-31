import pyttsx3


class Zuckbot:
    """Virtual reincarnation of Mark Zuckerberg."""


    def __init__(self):
        """Initializes Zuckbot class attributes."""
        self.tts_engine = pyttsx3.init()


    def speak(self):
        """Makes Zuckbot's text-to-speech engine say something random."""
        self.tts_engine.say("Hello, world!")
        self.tts_engine.runAndWait()