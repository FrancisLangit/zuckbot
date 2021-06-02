import pygame


class Footer:


    def __init__(self, gamestate):
        self.parent = gamestate
        self.settings = gamestate.settings
        self.screen = gamestate.screen
        self.screen_rect = gamestate.screen_rect

        self.copyright_text = _Footer_Text(
            self, 
            'MIT License • Copyright © 2021 • Francis Langit',
            {'bottomleft': self.screen_rect.bottomleft},
            25,
            -20
        )
        self.email_text = _Footer_Text(
            self, 
            'francis.villanueva.langit@gmail.com',
            {'bottomright': self.screen_rect.bottomright},
            -25,
            -20
        )


    def blitme(self):
        self.copyright_text.blitme()
        self.email_text.blitme()



class _Footer_Text:
    

    def __init__(self, parent, text, rect_alignment, x_offset, y_offset):
        self.parent = parent
        self.settings = parent.settings
        self.screen = parent.screen

        self.text = text
        self.rect_alignment = rect_alignment
        self.x_offset = x_offset
        self.y_offset = y_offset

        self.image = self._get_image()
        self.image_rect = self._get_image_rect()


    def _get_image(self):
        font = pygame.font.Font(
            self.settings.font_light_filename, 
            16,
        )
        font_image = font.render(
            self.text,
            True,
            self.settings.font_color,
        )
        return font_image 


    def _get_image_rect(self):
        image_rect = self.image.get_rect(**self.rect_alignment)
        image_rect.x += self.x_offset
        image_rect.y += self.y_offset
        return image_rect


    def blitme(self):
        self.screen.blit(self.image, self.image_rect)