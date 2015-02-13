import pygame


# This is like a mutable tuple to allow users to create a Point or Vector with labelled x and y components.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# This is a generic object in the Game World. It has a nice initializer to create the Sprite.
# It inherits from the pygame.sprite.Sprite class thus allowing all objects to be Sprites.
class Object(pygame.sprite.Sprite):
    def __init__(self, position, file_name):
        # Initialize the Sprite
        pygame.sprite.Sprite.__init__(self)
        # load the image, converting the pixel format for optimization
        self.image = pygame.image.load(file_name).convert()
        # make 'color' transparent on the image
        self.image.set_colorkey((0, 0, 0))
        # set the rectangle defined for this image for collision detection
        self.rect = self.image.get_rect()
        # position the image using the value passed.
        self.rect.center = (position.x, position.y)
        # Create a velocity variable for all objects.
        self.velocity = Point(0, 0)

    # Use this function every time the game needs to be updated for every object.
    # It ensures that object moves based on the velocity. Can be overridden by subclasses.
    def move(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
