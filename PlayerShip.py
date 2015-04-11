from Ship import *
from pygame.locals import *
from Globals import *
import math


# This is the player ship object in the Game World. It has a nice initializer to create the Ship.
# It inherits from the Ship class.
class PlayerShip(Ship):

    def __init__(self, position, folder_name):
        self.health = 200
        self.angle = 0.0
        self.folder_name = folder_name
        self.fuel = 0
        player_folder = str(folder_name) + "/PlayerShip" + str(self.angle) + ".png"
        Ship.__init__(self, position, player_folder, (ship_scale, ship_scale))

    # Overrides the Object's move so that rotating the ship is possible.
    def move(self, x_vel, screen_height):
        self.fuel = min(max_fuel, self.fuel)
        # Water Friction! - Idk what else to call it!
        friction = -self.velocity[1] * friction_ratio
        self.velocity = (self.velocity[0], self.velocity[1] + friction)
        if abs(self.velocity[1]) < 0.01:
            self.velocity = (self.velocity[0], 0)
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity = (self.velocity[0], max(0, self.velocity[1]))
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
            self.velocity = (self.velocity[0], min(0, self.velocity[1]))
        # Calculate angle using some good ol' Pythagorean Theorem
        new_angle = 0.0
        if self.velocity[1] != 0:
            number_of_images_used = (90 / angle_deviations) - 1  # This is calculated based on how many images we use.
            angle_proportion = math.ceil(abs(self.velocity[1]) / max_y_vel * number_of_images_used)
            new_angle = angle_proportion * angle_deviations  # Calculate the right angle based on image names
        if self.velocity[1] > 0 and new_angle != 0:  # Since we only checked for angles in the range [0, 90]
            new_angle = 360 - new_angle
        # if angle has changed than what it was before switch out the image and set some properties
        if self.angle != new_angle:
            self.angle = new_angle
            center_point = self.rect.center
            self.image = pygame.image.load(str(self.folder_name) + "/PlayerShip" + str(self.angle) + ".png")
            self.image = pygame.transform.scale(self.image, (ship_scale, ship_scale))  # Scale image
            self.image.set_colorkey((0, 0, 0, 0))
            # set the rectangle defined for this image for collision detection
            self.rect = self.image.get_rect()
            self.rect.center = center_point  # Reset the position
        Object.move(self)  # Call super.move so that everything gets updated like usual.

    # Use this method to update the health. It returns true if the player ship is alive and
    # false if the player ship has no health left.
    def damage(self, damage_done):
        self.health -= damage_done

    def input(self, keys):
        if keys[K_UP]:
            self.fuel -= reduce_fuel
            self.velocity = (self.velocity[0], self.velocity[1] - move_amount)
        if keys[K_DOWN]:
            self.fuel -= reduce_fuel
            self.velocity = (self.velocity[0], self.velocity[1] + move_amount)
        self.velocity = (self.velocity[0], min(max(min_y_vel, self.velocity[1]), max_y_vel))


def normalize_angle(x):
    new_angle = math.degrees(x)
    while new_angle < 0 or new_angle > 90:
        if new_angle < 0:
            new_angle += 90
        else:
            new_angle -= 90
    return new_angle