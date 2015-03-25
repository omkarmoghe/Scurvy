import pygame, random, sys
from pygame.locals import *

from main import *
from MainMenu import *

pygame.init()

def is_mouse_selection(checkbox, (posx, posy)):
        if (posx >= checkbox.left and posx <= checkbox.right) and \
            (posy >= checkbox.top and posy <= checkbox.bottom):
                return True
        return False

def check_keys(name,key):
    if len(name) > 0:
        if key == K_BACKSPACE:
            return name[:len(name)-1]
    if len(name) < 12:
        if key == K_a:
            return name + "A"
        if key == K_b:
            return name + "B"
        if key == K_c:
            return name + "C"
        if key == K_d:
            return name + "D"
        if key == K_e:
            return name + "E"
        if key == K_f:
            return name + "F"
        if key == K_g:
            return name + "G"
        if key == K_h:
            return name + "H"
        if key == K_i:
            return name + "I"
        if key == K_j:
            return name + "J"
        if key == K_k:
            return name + "K"
        if key == K_l:
            return name + "L"
        if key == K_m:
            return name + "M"
        if key == K_n:
            return name + "N"
        if key == K_o:
            return name + "O"
        if key == K_p:
            return name + "P"
        if key == K_q:
            return name + "Q"
        if key == K_r:
            return name + "R"
        if key == K_s:
            return name + "S"
        if key == K_t:
            return name + "T"
        if key == K_u:
            return name + "U"
        if key == K_v:
            return name + "V"
        if key == K_w:
            return name + "W"
        if key == K_x:
            return name + "X"
        if key == K_y:
            return name + "Y"
        if key == K_z:
            return name + "Z"
        if key == K_0:
            return name + "0"
        if key == K_1:
            return name + "1"
        if key == K_2:
            return name + "2"
        if key == K_3:
            return name + "3"
        if key == K_4:
            return name + "4"
        if key == K_5:
            return name + "5"
        if key == K_6:
            return name + "6"
        if key == K_7:
            return name + "7"
        if key == K_8:
            return name + "8"
        if key == K_9:
            return name + "9"
    return name

def show_Settings():
    quitStatus=0
    onSelected = 1
    textboxSelected=0
    cheat = ''
    
    while quitStatus != 1:
    
        pygame.display.set_caption('Settings')
        
             
        background_image = "Resources/Background.png" 
        background = pygame.image.load(background_image)
        backgroundRect = background.get_rect()
        WIDTH = backgroundRect.width
        HEIGHT = 3 * backgroundRect.height / 2
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        background_image = "Resources/MenuBackground.png" 
        background = pygame.image.load(background_image)
        screen.blit(background,backgroundRect)
        
        #creates the label at the top
        title_label = pygame.font.Font(font_file, 70).render('{0}'.format('Settings'),True, (255, 255, 255))
        title_rect = title_label.get_rect()
        title_rect.centerx = WIDTH * 1 / 2
        title_rect.centery = HEIGHT* 1 / 5
        screen.blit(title_label, title_rect)
        
        #creates the sound label
        sound_label = pygame.font.Font(font_file, 50).render('{0}'.format('Sound'),True, (255, 255, 255))
        sound_rect = sound_label.get_rect()
        sound_rect.centerx = WIDTH * 1 / 4
        sound_rect.centery = HEIGHT* 2 / 5
        screen.blit(sound_label, sound_rect)
        
        #creates the sound on label
        soundOn_label = pygame.font.Font(font_file, 30).render('{0}'.format('On'),True, (255, 255, 255))
        soundOn_rect = soundOn_label.get_rect()
        soundOn_rect.centerx = WIDTH * 1 / 4
        soundOn_rect.centery = HEIGHT* 3 / 5
        screen.blit(soundOn_label, soundOn_rect)
        
        #creates the sound off label
        soundOff_label = pygame.font.Font(font_file, 30).render('{0}'.format('Off'),True, (255, 255, 255))
        soundOff_rect = soundOff_label.get_rect()
        soundOff_rect.centerx = WIDTH * 1 / 4
        soundOff_rect.centery = HEIGHT* 5 / 7
        screen.blit(soundOff_label, soundOff_rect)
        
        #creates the unchecked on box, image from iconfinder.com from visual pharm
        checkbox_image = "Resources/UncheckedBox.png"
        checkbox = pygame.image.load(checkbox_image)
        checkbox = pygame.transform.scale(checkbox,(40,40))
        checkboxRect = checkbox.get_rect()
        checkboxRect.centerx = WIDTH * 1 / 3
        checkboxRect.centery = HEIGHT * 3 / 5
        checkboxRect.left = checkboxRect.centerx-20
        checkboxRect.right = checkboxRect.centerx+20
        checkboxRect.top = checkboxRect.centery-20
        checkboxRect.bottom = checkboxRect.centery+20
        
        #creates the unchecked off box, image from iconfinder.com from visual pharm
        checkbox2_image = "Resources/UncheckedBox.png"
        checkbox2 = pygame.image.load(checkbox2_image)
        checkbox2 = pygame.transform.scale(checkbox2,(40,40))
        checkbox2Rect = checkbox2.get_rect()
        checkbox2Rect.centerx = WIDTH * 1 / 3
        checkbox2Rect.centery = HEIGHT * 5 / 7
        checkbox2Rect.left = checkbox2Rect.centerx-20
        checkbox2Rect.right = checkbox2Rect.centerx+20
        checkbox2Rect.top = checkbox2Rect.centery-20
        checkbox2Rect.bottom = checkbox2Rect.centery+20
        
        #creates the checked on box, image from iconfinder.com from visual pharm
        checkboxSelected_image = "Resources/CheckedBox.png"
        checkboxSelected = pygame.image.load(checkboxSelected_image)
        checkboxSelected = pygame.transform.scale(checkboxSelected,(40,40))
        checkboxSelectedRect = checkboxSelected.get_rect()
        checkboxSelectedRect.centerx = WIDTH * 1 / 3
        checkboxSelectedRect.centery = HEIGHT * 3 / 5
        checkboxSelectedRect.left = checkboxSelectedRect.centerx-20
        checkboxSelectedRect.right = checkboxSelectedRect.centerx+20
        checkboxSelectedRect.top = checkboxSelectedRect.centery-20
        checkboxSelectedRect.bottom = checkboxSelectedRect.centery+20
        
        #creates the checked off box, image from iconfinder.com from visual pharm
        checkboxSelected2_image = "Resources/CheckedBox.png"
        checkboxSelected2 = pygame.image.load(checkboxSelected2_image)
        checkboxSelected2 = pygame.transform.scale(checkboxSelected2,(40,40))
        checkboxSelected2Rect = checkboxSelected2.get_rect()
        checkboxSelected2Rect.centerx = WIDTH * 1 / 3
        checkboxSelected2Rect.centery = HEIGHT * 5 / 7
        checkboxSelected2Rect.left = checkboxSelected2Rect.centerx-20
        checkboxSelected2Rect.right = checkboxSelected2Rect.centerx+20
        checkboxSelected2Rect.top = checkboxSelected2Rect.centery-20
        checkboxSelected2Rect.bottom = checkboxSelected2Rect.centery+20
        
        #creates the cheats label
        cheats_label = pygame.font.Font(font_file, 50).render('{0}'.format('Cheats'),True, (255, 255, 255))
        cheats_rect = cheats_label.get_rect()
        cheats_rect.centerx = WIDTH * 3 / 4
        cheats_rect.centery = HEIGHT* 2 / 5
        screen.blit(cheats_label, cheats_rect)
        
        cheatsname_label = pygame.font.Font(font_file, 25).render('{0}'.format(cheat),True, (0,0,0))
        cheatsname_rect = cheatsname_label.get_rect()
        cheatsname_rect.left = WIDTH * 3 / 5 + 15
        cheatsname_rect.centery = HEIGHT* 3 / 5
        
        
        #creates the cheats text box
        textbox_image = "Resources/textBox.png"
        textbox = pygame.image.load(textbox_image)
        textboxRect = textbox.get_rect()
        textboxRect.centerx = WIDTH * 3 / 4
        textboxRect.centery = HEIGHT * 3 / 5
        textboxRect.left = textboxRect.centerx-110
        textboxRect.right = textboxRect.centerx+110
        textboxRect.top = textboxRect.centery-30
        textboxRect.bottom = textboxRect.centery+30
        
        #creates the cheats text highlighted box
        textboxHighlighted_image = "Resources/textBoxHighlighted.png"
        textboxHighlighted = pygame.image.load(textboxHighlighted_image)
        textboxHighlightedRect = textboxHighlighted.get_rect()
        textboxHighlightedRect.centerx = WIDTH * 3 / 4
        textboxHighlightedRect.centery = HEIGHT * 3 / 5
        textboxHighlightedRect.left = textboxHighlightedRect.centerx-110
        textboxHighlightedRect.right = textboxHighlightedRect.centerx+110
        textboxHighlightedRect.top = textboxHighlightedRect.centery-30
        textboxHighlightedRect.bottom = textboxHighlightedRect.centery+30
        
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
        
        
        if onSelected == 1:
            screen.blit(checkboxSelected, checkboxSelectedRect)
            screen.blit(checkbox2, checkbox2Rect)
        if onSelected == 0:
            screen.blit(checkboxSelected2, checkboxSelected2Rect)
            screen.blit(checkbox, checkboxRect)
        if textboxSelected == 0:
            screen.blit(textbox, textboxRect)
        if textboxSelected == 1:
            screen.blit(textboxHighlighted, textboxHighlightedRect)
            
        mpos = pygame.mouse.get_pos()
        #checks to see if the user quits
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                tf = open("sound_and_cheat.txt",'w')
                if onSelected==1:
                    onSelected="On"
                else:
                    onSelected="Off"
                tf.write("%s\n%s" % (onSelected, cheat))
                tf.close()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_mouse_selection(backButtonRect,mpos):
                    return
                if is_mouse_selection(textboxRect,mpos):
                    textboxSelected = 1
                if onSelected==1 and is_mouse_selection(checkbox2Rect,mpos):
                    onSelected=0
                elif onSelected==0 and is_mouse_selection(checkboxRect,mpos):
                    onSelected=1
            
            if event.type == KEYDOWN:
                if textboxSelected == 1:
                    cheat = check_keys(cheat, event.key)
                    
         
        screen.blit(cheatsname_label,cheatsname_rect)
        
        
        pygame.display.flip()
        
    