from Ship import *
from Point import *
from pygame.locals import *
import math

ship_scale = 150  # Adjust this to change the size of the ship.
angle_deviations = 22.5  # Adjust this value if we get more images.
friction_ratio = 0.25  # Adjust this value to change the dynamic friction proportion
max_y_vel = 2.5  # Adjust this value to change the fastest a boat can move.
min_y_vel = -max_y_vel  # DO NOT adjust this value. It is determined dynamically based on the max velocity
move_amount = 0.3  # Adjust this value to change the acceleration of the boat.


# This is the player ship object in the Game World. It has a nice initializer to create the Ship.
# It inherits from the Ship class.
class PlayerShip(Ship):

    def __init__(self, position, folder_name):
        self.health = 200
        self.angle = 0.0
        self.folder_name = folder_name
        player_folder = str(folder_name) + "/PlayerShip" + str(self.angle) + ".png"
        Ship.__init__(self, position, player_folder, Point(ship_scale, ship_scale))

    # Overrides the Object's move so that rotating the ship is possible.
    def move(self, x_vel, screen_height):
        # Water Friction! - Idk what else to call it!
        friction = -self.velocity.y * friction_ratio
        self.velocity.y += friction
        if abs(self.velocity.y) < 0.01:
            self.velocity.y = 0
        if self.rect.top <= 0:
            self.rect.top = 0
            self.velocity.y = max(0, self.velocity.y)
        if self.rect.bottom >= screen_height:
            self.rect.bottom = screen_height
            self.velocity.y = min(0, self.velocity.y)
        # Calculate angle using some good ol' Pythagorean Theorem
        # print "Velocity : (" + str(x_vel / self.ratio) + ", " + str(-self.velocity.y) + ")"
        # self.image = pygame.transform.rotate(self.image, actual_angle)
        # self.rect = self.image.get_rect()
        # self.rect.center = center_point
        # FIXME: This needs to be fixed to fix the random spasms of the boat.
        '''actual_angle = normalize_angle(math.tan(-self.velocity.y / (x_vel / self.ratio)))
        new_angle = actual_angle / angle_deviations
        # Find closest value to angle_deviations so that everything works
        # print "Raw new angle is " + str(new_angle)
        if new_angle - math.floor(new_angle) >= 0.5:
            new_angle = math.ceil(new_angle)
        else:
            new_angle = math.floor(new_angle)
        new_angle *= angle_deviations
        if new_angle == -0.0:
            new_angle = 0.0 '''
        new_angle = 0.0
        if self.velocity.y != 0:
            number_of_images_used = (90 / angle_deviations) - 1  # This is calculated based on how many images we use.
            angle_proportion = math.ceil(abs(self.velocity.y) / max_y_vel * number_of_images_used)
            new_angle = angle_proportion * angle_deviations  # Calculate the right angle based on image names
        # print "New angle is " + str(new_angle) + " and the old angle is " + str(self.angle)
        if self.velocity.y > 0 and new_angle != 0:  # Since we only checked for angles in the range [0, 90]
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
            self.velocity.y -= move_amount
        if keys[K_DOWN]:
            self.velocity.y += move_amount
        self.velocity.y = min(max(min_y_vel, self.velocity.y), max_y_vel)


def normalize_angle(x):
    new_angle = math.degrees(x)
    while new_angle < 0 or new_angle > 90:
        if new_angle < 0:
            new_angle += 90
        else:
            new_angle -= 90
    return new_angle