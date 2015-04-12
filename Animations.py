from Globals import *


fps = 20


def generate_animation_images((width, height), filename):
    # images array will be filled with each frame of an animation
    images = []

    full_image = pygame.image.load(filename).convert_alpha()
    full_width, full_height = full_image.get_size()

    for i in xrange(int(full_width / width)):
        images.append(full_image.subsurface((i*width, 0, width, height)))
    return images


class Animations(pygame.sprite.Sprite):

    def __init__(self, (width, height), filename, location):
        pygame.sprite.Sprite.__init__(self)

        self.all_images = generate_animation_images((width, height), filename)
        # delay is time between animation frames
        # last_update saves the time the animation was last updated
        self.delay = 1000/fps
        self.last_update = 0
 
        # frame is the array location in images
        self.frame = 0
        self.location = location
        
        # sets the animations current image
        self.image = self.all_images[self.frame]
        self.rect = self.image.get_rect()
        
    # This method updates the animation image
    def update_animation(self, total_time):
        # checks if enough time has passed to change the image
        if total_time - self.last_update > self.delay:
            self.frame += 1
            
            # checks if the new image is greater than the number of images
            # starts image cycle over if true
            if self.frame >= len(self.all_images): 
                self.frame = 0
                
            # updates current animation image
            self.image = self.all_images[self.frame]
            
            # changes the last update time
            self.last_update = total_time

        # draws animation changes to the screen
        screen.blit(self.image, self.location)

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.location[0]
        self.rect.y = self.location[1]
        screen.blit(self.image, self)