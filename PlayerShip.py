from Ship import *
from Point import *

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
    def move(self, instruction_completed, move_to_y):
        max_y_speed = 10
        if instruction_completed:
            if move_to_y > self.rect.y:
                self.velocity.y += max_y_speed
            elif move_to_y < self.rect.y:
                self.velocity.y -= max_y_speed
        super.move(self)
        # TODO: Calculate rotation and choose correct image
        # angle = something other than what it was before.
        # new image = folder name + PlayerShip + angle.png"

    # Use this method to update the health. It returns true if the player ship is alive and
    # false if the player ship has no health left.
    def damage(self, damage_done):
        self.health -= damage_done
        if (self.health <= 0):
            return False
        return True