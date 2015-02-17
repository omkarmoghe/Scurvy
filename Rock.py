from Object import *
from Point import *


class Rock(Object):
    def __init__(self, position):
        Object.__init__(self, position, "Resources/Rock.png", 1.0, Point(0, 0))

    def move(self, screen_width):
        Object.move(self)
        if self.rect.right <= 0:
            self.reset_position(screen_width)

    def reset_position(self, screen_width):
        self.rect.left = screen_width

    def check_collision(self, ship):
        if pygame.sprite.collide_rect(self, ship):
            return True  # HEALTH LOST HERE
        return False