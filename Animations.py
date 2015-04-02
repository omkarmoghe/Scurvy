import pygame,os,random,time
from pygame.locals import *
from Object import *
from Gameplay import *


fps = 10

def AnimationImages(width, height, filename):
    # images array will be filled with each frame of an animation
    images = []

    fullImage = pygame.image.load(filename).convert_alpha()
    fullWidth, fullHeight = fullImage.get_size()

    for i in xrange(int(fullWidth/width)):
        images.append(fullImage.subsurface((i*width, 0, width ,height)))
    return images


class Animations(pygame.sprite.Sprite):

    def __init__(self, width, height, filename, location, screen):
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.all_images = AnimationImages(width, height, filename)
 
        # delay is time between animation frames
        # last_update saves the time the animation was last updated
        self.delay = 1000/fps
        self.last_update = 0
 
        # frame is the array location in images
        self.frame = 0
        self.location = location
        
        # sets the animations current image
        self.image = self.all_images[self.frame]
        
    # This method updates the animation image
    def updateAnimation (self, totalTime):
        
        # checks if enough time has passed to change the image
        if totalTime - self.last_update > self.delay:
            self.frame += 1
            
            # checks if the new image is greater than the number of images
            # starts image cycle over if true
            if self.frame >= len(self.all_images): 
                self.frame = 0
                
            # updates current animation image
            self.image = self.all_images[self.frame]
            
            # changes the last update time
            self.last_update = totalTime

        # draws animation changes to the screen
        self.screen.blit(self.image, self.location)

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.location[0]
        self.rect.y = self.location[1]
        self.screen.blit(self.image, self)