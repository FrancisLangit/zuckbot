import pygame

from .objects.question_input import Question_Input
from .objects.zuckbot import Zuckbot


class Game_Screen:
    """Gamestate where user interacts with Zuckbot."""


    def __init__(self, main):
        """Initialize Game_Screen class attributes."""
        self.main = main
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.question_input = Question_Input(self)
        self.zuckbot = Zuckbot(self)

        self.is_running = False


    def _exit_to_title_screen(self):
        """Resets gamestate's objects and switches to title screen."""
        self.question_input.reset()
        self.zuckbot.reset()
        self.main.switch_gamestate(self, self.main.title_screen)


    def _validate_question(self):
        """Checks user's inputted question. If question input is not blank 
        and if Zuckbot isn't currently answering, Zuckbot responds and input 
        field is cleared."""
        if not self.question_input.is_blank() and not pygame.mixer.get_busy():
            self.zuckbot.answer()
            self.question_input.text_input.clear_text()


    def _check_keydown_events(self, event):
        """Checks keydown events of the gamestate."""
        if event.key == pygame.K_ESCAPE:
            self._exit_to_title_screen()
        if event.key == pygame.K_RETURN:
            self._validate_question()


    def _check_events(self, events):
        """Checks events of the gamestate."""
        for event in events:
            if event.type == pygame.QUIT:
                self.is_running = False
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                

    def run_gamestate(self):
        """Runs the game loop of the gamestate."""
        while self.is_running:
            self.screen.fill(self.settings.screen_background_color)

            events = pygame.event.get()
            self._check_events(events)

            self.question_input.update(events)
            self.zuckbot.update()

            self.question_input.blitme()
            self.zuckbot.blitme()

            pygame.display.flip()
