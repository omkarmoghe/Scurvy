import pygame
import Point


# This is a generic object in the Game World. It has a nice initializer to create the Sprite.
# It inherits from the pygame.sprite.Sprite class thus allowing all objects to be Sprites.
class Object(pygame.sprite.Sprite):

    def __init__(self, position, file_name, velocity_ratio, image_size):
        # Initialize the Sprite
        pygame.sprite.Sprite.__init__(self)
        # load the image, converting the pixel format for optimization
        self.image = pygame.image.load(file_name)
        if image_size.x != 0 and image_size.y != 0:
            self.image = pygame.transform.scale(self.image, (image_size.x, image_size.y))
        # make 'color' transparent on the image
        self.image.set_colorkey((0, 0, 0, 0))
        # set the rectangle defined for this image for collision detection
        self.rect = self.image.get_rect()
        # position the image using the value passed.
        self.rect.center = (position.x, position.y)
        # Create a velocity variable for all objects.
        self.velocity = Point.Point(0, 0)
        # This is the velocity ratio that enables parallax motion.
        self.ratio = velocity_ratio

    # Use this function every time the game needs to be updated for every object.
    # It ensures that object moves based on the velocity. Can be overridden by subclasses.
    def move(self):
        self.rect.x += round(self.velocity.x * self.ratio)
        self.rect.y += round(self.velocity.y * self.ratio)
