import pygame


class Zuckbot_Answers:
    """Holds methods associated with generating an array filled with 
    dictionaries each representing one of Zuckbot's answers.""" 


    def _get_answer_dict(self, answer_name, answer_text):
        """Returns a dictionary holding the sound, image, and text to be shown 
        for one of Zuckbot's answers.
        
        Arguments:
            answer_name (str) : Name of the audio and image file.
            answer_text (str) : Text of the answer to be displayed.
        """
        return {
            'sound': pygame.mixer.Sound(f'data/audio/{answer_name}.wav'),
            'image': pygame.image.load(f'data/images/{answer_name}.jpg'),
            'text': answer_text,
        }


    def get(self):
        """Returns an array of answer dictionaries."""
        return [
            # Affirmatives
            self._get_answer_dict(
                'zuckbot_affirmative_1', 
                "I don't see why that isn't possible."
            ),
            self._get_answer_dict(
                'zuckbot_affirmative_2', 
                 "It's almost a disadvantage if you're not on it now.",
            ),
            self._get_answer_dict(
                'zuckbot_affirmative_3', 
                'Sure, if you do the things that are easier first.',
            ),
            self._get_answer_dict(
                'zuckbot_affirmative_4', 
                "There's a lot of that in Silicon Valley.",
            ),
            self._get_answer_dict(
                'zuckbot_affirmative_5', 
                "Yes, I believe that that's correct.",
            ),

            # Negatives
            self._get_answer_dict(
                'zuckbot_negative_1', 
                'A squirrel dying in front of your house may be more relevant.',
            ),
            self._get_answer_dict(
                'zuckbot_negative_2',
                "Certainly doesn't feel like that to me.",
            ),
            self._get_answer_dict(
                'zuckbot_negative_3', 
                'I think that is somewhat of a burden.',
            ),
            self._get_answer_dict(
                'zuckbot_negative_4', 
                "No.",
            ),
            self._get_answer_dict(
                'zuckbot_negative_5', 
                "No, I would not choose to do that publicly here.",
            ),

            # Non-comittals
            self._get_answer_dict(
                'zuckbot_noncomittal_1', 
                "Can't really give you an answer to that one.",
            ),
            self._get_answer_dict(
                'zuckbot_noncomittal_2', 
                "I don't know the answer to that off the top of my head.",
            ),
            self._get_answer_dict(
                'zuckbot_noncomittal_3', 
                'I hope not.',
            ),
            self._get_answer_dict(
                'zuckbot_noncomittal_4', 
                "I'm not sure what that means.",
            ),
            self._get_answer_dict(
                'zuckbot_noncomittal_5', 
                "I'm not sure of the answer to that question.",
            ),
            self._get_answer_dict(
                'zuckbot_noncomittal_6', 
                'Maybe.',
            ),
            self._get_answer_dict(
                'zuckbot_noncomittal_7', 
                'This is a complex issue that deserves more than one word.',
            ),
            self._get_answer_dict(
                'zuckbot_noncomittal_8', 
                "Can't answer right now. Too much sunscreen on my face.",
            ),
            self._get_answer_dict(
                'zuckbot_noncomittal_9', 
                "Hold on, I'll ask my legal counsel first.",
            ),
            self._get_answer_dict(
                'zuckbot_noncomittal_10', 
                "We'll get back to you on that.",
            ),
        ]