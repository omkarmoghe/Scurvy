import pygame


# This is a generic object in the Game World. It has a nice initializer to create the Sprite.
# It inherits from the Sprite class thus allowing all objects to be Sprites.
class Object(pygame.sprite.Sprite):

    def __init__(self, position, file_name, velocity_ratio, image_size):
        # Initialize the Sprite
        pygame.sprite.Sprite.__init__(self)
        # load the image, converting the pixel format for optimization
        self.image = pygame.image.load(file_name)
        if image_size[0] != 0 and image_size[1] != 0:
            self.image = pygame.transform.scale(self.image, (image_size[0], image_size[1]))
        # make 'color' transparent on the image
        self.image.set_colorkey((0, 0, 0, 0))
        # make a mask based on the image.
        self.mask = pygame.mask.from_surface(self.image)
        # set the rectangle defined for this image for collision detection
        self.rect = self.image.get_rect()
        # position the image using the value passed.
        self.rect.center = (position[0], position[1])
        # Create a velocity variable for all objects.
        self.velocity = (0, 0)
        # This is the velocity ratio that enables parallax motion.
        self.ratio = velocity_ratio

    # Use this function every time the game needs to be updated for every object.
    # It ensures that object moves based on the velocity. Can be overridden by subclasses.
    def move(self):
        self.rect.x += round(self.velocity[0] * self.ratio)
        self.rect.y += round(self.velocity[1] * self.ratio)
