import pygame

from .objects.question_input import Question_Input


class Game_Screen:
    """Gamestate where user interacts with Zuckbot."""


    def __init__(self, main):
        """Initialize Game_Screen class attributes."""
        self.main = main
        self.settings = main.settings
        self.screen = main.screen
        self.screen_rect = main.screen_rect

        self.question_input = Question_Input(self)

        self.is_running = False


    def _check_keydown_events(self, event):
        """Checks of keydown events of the gamestate."""
        if event.key == pygame.K_ESCAPE:
            self.question_input.reset()
            self.is_running = False
            self.main.title_screen.is_running = True
            self.main.title_screen.run_gamestate()
        if event.key == pygame.K_RETURN:
            self.question_input.text_input.clear_text()


    def run_gamestate(self):
        """Runs the game loop of the gamestate."""
        while self.is_running:
            self.screen.fill(self.settings.screen_background_color)
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)

            self.question_input.update(events)
            self.question_input.blitme()

            pygame.display.update()