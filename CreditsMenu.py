import pygame, random, sys
from pygame.locals import *

from main import *

pygame.init()

def is_mouse_selection(checkbox, (posx, posy)):
        if (posx >= checkbox.left and posx <= checkbox.right) and \
            (posy >= checkbox.top and posy <= checkbox.bottom):
                return True
        return False

def show_Credits():
    quitStatus=0
    while quitStatus != 1:
    
        pygame.display.set_caption('Credits')
        
                
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
        
        infile = open("copyright.txt","r")
        array = infile.readlines()
        
        for (i, credit) in enumerate(array):
            credit = credit[:len(credit)-1]
            credit_label = pygame.font.Font(font_file, 15).render('{0}'.format(credit),
                                                                       True, (255,255,255))
            credit_label_rect = credit_label.get_rect()
            credit_label_rect.left = WIDTH*1/10
            credit_label_rect.centery = HEIGHT * 2/5 + i*20
            screen.blit(credit_label, credit_label_rect)
            
        
        backButton_image = "Resources/backButton.png"
        backButton = pygame.image.load(backButton_image)
        backButton = pygame.transform.scale(backButton,(60,60))
        backButtonRect = backButton.get_rect()
        backButtonRect.centerx = 50
        backButtonRect.centery = 50
        backButtonRect.left = backButtonRect.centerx-30
        backButtonRect.right = backButtonRect.centerx+30
        backButtonRect.top = backButtonRect.centery-30
        backButtonRect.bottom = backButtonRect.centery+30
        screen.blit(backButton, backButtonRect)
        
        mpos = pygame.mouse.get_pos()
         #checks to see if the user quits
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_mouse_selection(backButtonRect,mpos):
                    return
            
        pygame.display.flip()