import pygame, random, sys
from pygame.locals import *

from main import *

pygame.init()

def show_Credits():
    quitStatus=0
    while quitStatus != 1:
    
        pygame.display.set_caption('Credits')
        
        
        #checks to see if the user quits
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
                
        background_image = "Resources/Background.png" 
        background = pygame.image.load(background_image)
        backgroundRect = background.get_rect()
        WIDTH = backgroundRect.width
        HEIGHT = 3 * backgroundRect.height / 2
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        background_image = "Resources/MenuBackground.png" 
        background = pygame.image.load(background_image)
        screen.blit(background,backgroundRect)
        
        title_label = pygame.font.Font(font_file, 70).render('{0}'.format('Credits'),
                                                                       True, (255, 255, 255))
        title_rect = title_label.get_rect()
        title_rect.centerx = WIDTH * 1 / 2
        title_rect.centery = HEIGHT* 1 / 5
        screen.blit(title_label, title_rect)
        
        pygame.display.flip()