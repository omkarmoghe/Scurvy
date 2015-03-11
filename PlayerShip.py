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
    def move(self, x_vel):
        # TODO: Calculate rotation and choose correct image
        # angle = something other than what it was before.
        # new image = folder name + PlayerShip + angle.png"
        super.move(self)

    # Use this method to update the health. It returns true if the player ship is alive and
    # false if the player ship has no health left.
    def damage(self, damage_done):
        self.health -= damage_done

    def input(self, keys):
        max_y_vel = 50
        min_y_vel = -max_y_vel
        move_amount = 10
        for key in keys:
            if key == pygame.K_UP:
                self.velocity.y -= move_amount
                # TODO: Move up
            elif key == pygame.K_DOWN:
                self.velocity.y += move_amount
                # TODO: Move down
        self.velocity.y = min(max(min_y_vel, self.velocity.y), min_y_vel)