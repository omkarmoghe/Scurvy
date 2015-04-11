import pygame
from pygame.locals import *


def check_keys(name, key):
    if len(name) > 0:
        if key == K_BACKSPACE:
            return name[:len(name)-1]
    if len(name) < 12:
        if len(pygame.key.name(key)) == 1:
            return (name + pygame.key.name(key)).upper()
    return name.upper()


class ControlBox(pygame.sprite.Sprite):
    def __init__(self, image, selected_image, pos, scale, selected=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.selected_image = None
        if selected_image is not None:
            self.selected_image = pygame.image.load(selected_image)
        if scale is not None:
            self.image = pygame.transform.scale(self.image, scale)
            if selected_image is not None:
                self.selected_image = pygame.transform.scale(self.selected_image, scale)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.selected = selected

    def is_mouse_selection(self, (pos_x, pos_y)):
        if self.rect.collidepoint(pos_x, pos_y):
            self.selected = True
            return True
        return False

    def get_image(self):
        if self.selected:
            return self.selected_image
        else:
            return self.image
