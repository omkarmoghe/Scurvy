from Ship import *
from Point import *
from pygame.locals import *


# This is the player ship object in the Game World. It has a nice initializer to create the Ship.
# It inherits from the Ship class.
class PlayerShip(Ship):

    def __init__(self, position, folder_name):
        self.health = 200
        self.angle = 0
        self.folder_name = folder_name
        player_folder = str(folder_name) + "/PlayerShip" + str(self.angle) + ".png"
        Ship.__init__(self, position, player_folder, Point(150, 150))

    # Overrides the Object's move so that rotating the ship is possible.
    def move(self, x_vel, screen_height):
        # TODO: Calculate rotation and choose correct image based on x_vel and self.velocity.y
        # angle = something other than what it was before.
        # new image = folder name + PlayerShip + angle.png"
        # Water Friction! - Idk what else to call it.
        friction = -self.velocity.y * 0.25
        self.velocity.y += friction
        if abs(self.velocity.y) < 0.5:
            self.velocity.y = 0
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity.y = max(0, self.velocity.y)
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
            self.velocity.y = min(0, self.velocity.y)
        Object.move(self)

    # Use this method to update the health. It returns true if the player ship is alive and
    # false if the player ship has no health left.
    def damage(self, damage_done):
        self.health -= damage_done

    def input(self, keys):
        max_y_vel = 5
        min_y_vel = -max_y_vel
        move_amount = 1
        if keys[K_UP]:
            self.velocity.y -= move_amount
            # TODO: Move up
        if keys[K_DOWN]:
            self.velocity.y += move_amount
            # TODO: Move down
        self.velocity.y = min(max(min_y_vel, self.velocity.y), max_y_vel)