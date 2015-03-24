import pygame, random, sys
from pygame.locals import *

from main import *

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
       
  
    


def show_Customization():
    quitStatus=0
    easySelected=1
    textboxSelected=0
    player1name = ''
    player2name = ''
    while quitStatus != 1:
        pygame.display.set_caption('Customization Menu')
        
        
                
        background_image = "Resources/Background.png" 
        background = pygame.image.load(background_image)
        backgroundRect = background.get_rect()
        WIDTH = backgroundRect.width
        HEIGHT = 3 * backgroundRect.height / 2
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        background_image = "Resources/MenuBackground.png" 
        background = pygame.image.load(background_image)
        screen.blit(background,backgroundRect)
        
        title_label = pygame.font.Font(font_file, 70).render('{0}'.format('Customization'),
                                                                       True, (255, 255, 255))
        title_rect = title_label.get_rect()
        title_rect.centerx = WIDTH * 1 / 2
        title_rect.centery = HEIGHT* 1 / 5
        screen.blit(title_label, title_rect)
        
         #creates the sound label
        difficulty_label = pygame.font.Font(font_file, 50).render('{0}'.format('Difficulty'),True, (255, 255, 255))
        difficulty_rect = difficulty_label.get_rect()
        difficulty_rect.centerx = WIDTH * 1 / 4
        difficulty_rect.centery = HEIGHT* 2 / 5
        screen.blit(difficulty_label, difficulty_rect)
        
        #creates the sound on label
        easy_label = pygame.font.Font(font_file, 30).render('{0}'.format('Easy'),True, (255, 255, 255))
        easy_rect = easy_label.get_rect()
        easy_rect.centerx = WIDTH * 1 / 5
        easy_rect.centery = HEIGHT* 3 / 5
        screen.blit(easy_label, easy_rect)
        
        #creates the sound off label
        hard_label = pygame.font.Font(font_file, 30).render('{0}'.format('Hard'),True, (255, 255, 255))
        hard_rect = hard_label.get_rect()
        hard_rect.centerx = WIDTH * 1 / 5
        hard_rect.centery = HEIGHT* 5 / 7
        screen.blit(hard_label, hard_rect)
        
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
        checkbox2 = pygame.image.load(checkbox_image)
        checkbox2 = pygame.transform.scale(checkbox2,(40,40))
        checkbox2Rect = checkbox2.get_rect()
        checkbox2Rect.centerx = WIDTH * 1 / 3
        checkbox2Rect.centery = HEIGHT * 5 / 7
        checkbox2Rect.left = checkbox2Rect.centerx-20
        checkbox2Rect.right = checkbox2Rect.centerx+20
        checkbox2Rect.top = checkbox2Rect.centery-20
        checkbox2Rect.bottom = checkbox2Rect.centery+20
        
        #creates the checked on box, image from iconfinder.com from visual pharm, icons8.com
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
        checkboxSelected2 = pygame.image.load(checkboxSelected_image)
        checkboxSelected2 = pygame.transform.scale(checkboxSelected2,(40,40))
        checkboxSelected2Rect = checkboxSelected2.get_rect()
        checkboxSelected2Rect.centerx = WIDTH * 1 / 3
        checkboxSelected2Rect.centery = HEIGHT * 5 / 7
        checkboxSelected2Rect.left = checkboxSelected2Rect.centerx-20
        checkboxSelected2Rect.right = checkboxSelected2Rect.centerx+20
        checkboxSelected2Rect.top = checkboxSelected2Rect.centery-20
        checkboxSelected2Rect.bottom = checkboxSelected2Rect.centery+20
        
        #creates the names label
        names_label = pygame.font.Font(font_file, 50).render('{0}'.format('Names'),True, (255, 255, 255))
        names_rect = names_label.get_rect()
        names_rect.centerx = WIDTH * 3 / 4
        names_rect.centery = HEIGHT* 2 / 5
        screen.blit(names_label, names_rect)
        
        #creates the player 1 label
        player1_label = pygame.font.Font(font_file, 30).render('{0}'.format('Player 1'),True, (255, 255, 255))
        player1_rect = player1_label.get_rect()
        player1_rect.centerx = WIDTH * 3 / 5
        player1_rect.centery = HEIGHT* 3 / 5
        screen.blit(player1_label, player1_rect)
        
        #creates the player 2 label
        player2_label = pygame.font.Font(font_file, 30).render('{0}'.format('Player 2'),True, (255, 255, 255))
        player2_rect = player2_label.get_rect()
        player2_rect.centerx = WIDTH * 3 / 5
        player2_rect.centery = HEIGHT* 5 / 7
        screen.blit(player2_label, player2_rect)
        
        #creates the player 1 name label
        player1name_label = pygame.font.Font(font_file, 25).render('{0}'.format(player1name),True, (0,0,0))
        player1name_rect = player1name_label.get_rect()
        player1name_rect.left = WIDTH * 5 / 7 + 10
        player1name_rect.centery = HEIGHT* 3 / 5
        
        #creates the player 2 name label
        player2name_label = pygame.font.Font(font_file, 25).render('{0}'.format(player2name),True, (0,0,0))
        player2name_rect = player2name_label.get_rect()
        player2name_rect.left = WIDTH * 5 / 7 + 10
        player2name_rect.centery = HEIGHT* 5 / 7
        
        
        #creates the player 1 box
        textbox_image = "Resources/textBox.png"
        textbox = pygame.image.load(textbox_image)
        textboxRect = textbox.get_rect()
        textboxRect.centerx = WIDTH * 6 / 7
        textboxRect.centery = HEIGHT * 3 / 5
        textboxRect.left = textboxRect.centerx-110
        textboxRect.right = textboxRect.centerx+110
        textboxRect.top = textboxRect.centery-30
        textboxRect.bottom = textboxRect.centery+30
        
        #creates the player 2 box
        textbox2 = pygame.image.load(textbox_image)
        textbox2Rect = textbox2.get_rect()
        textbox2Rect.centerx = WIDTH * 6 / 7
        textbox2Rect.centery = HEIGHT * 5 / 7
        textbox2Rect.left = textbox2Rect.centerx-110
        textbox2Rect.right = textbox2Rect.centerx+110
        textbox2Rect.top = textbox2Rect.centery-30
        textbox2Rect.bottom = textbox2Rect.centery+30
        
        #creates the player 1 highlighted box
        textboxHighlighted_image = "Resources/textBoxHighlighted.png"
        textboxHighlighted = pygame.image.load(textboxHighlighted_image)
        textboxHighlightedRect = textboxHighlighted.get_rect()
        textboxHighlightedRect.centerx = WIDTH * 6 / 7
        textboxHighlightedRect.centery = HEIGHT * 3 / 5
        textboxHighlightedRect.left = textboxHighlightedRect.centerx-110
        textboxHighlightedRect.right = textboxHighlightedRect.centerx+110
        textboxHighlightedRect.top = textboxHighlightedRect.centery-30
        textboxHighlightedRect.bottom = textboxHighlightedRect.centery+30
        
        #creates the player 2 highlighted box
        textboxHighlighted2 = pygame.image.load(textboxHighlighted_image)
        textboxHighlighted2Rect = textboxHighlighted2.get_rect()
        textboxHighlighted2Rect.centerx = WIDTH * 6 / 7
        textboxHighlighted2Rect.centery = HEIGHT * 5 / 7
        textboxHighlighted2Rect.left = textboxHighlighted2Rect.centerx-110
        textboxHighlighted2Rect.right = textboxHighlighted2Rect.centerx+110
        textboxHighlighted2Rect.top = textboxHighlighted2Rect.centery-30
        textboxHighlighted2Rect.bottom = textboxHighlighted2Rect.centery+30
        
        
        
        
        
        play_label = pygame.font.Font(font_file, 50).render('{0}'.format('Play!'),True, (255, 255, 255))
        play_rect = play_label.get_rect()
        play_rect.centerx = WIDTH * 1 / 2
        play_rect.centery = HEIGHT* 5 / 6
        screen.blit(play_label, play_rect)
        
        playButton_image = "Resources/StartButton.png"
        playButton = pygame.image.load(playButton_image)
        playButton = pygame.transform.scale(playButton,(60,60))
        playButtonRect = playButton.get_rect()
        playButtonRect.centerx = WIDTH * 1 / 2
        playButtonRect.centery = HEIGHT * 14 / 15
        playButtonRect.left = playButtonRect.centerx-30
        playButtonRect.right = playButtonRect.centerx+30
        playButtonRect.top = playButtonRect.centery-30
        playButtonRect.bottom = playButtonRect.centery+30
        screen.blit(playButton, playButtonRect)
        
        
        if easySelected == 1:
            screen.blit(checkboxSelected, checkboxSelectedRect)
            screen.blit(checkbox2, checkbox2Rect)
        if easySelected == 0:
            screen.blit(checkboxSelected2, checkboxSelected2Rect)
            screen.blit(checkbox, checkboxRect)
    
        if textboxSelected == 0:
            screen.blit(textbox2, textbox2Rect)
            screen.blit(textbox, textboxRect)
        if textboxSelected == 1:
            screen.blit(textboxHighlighted, textboxHighlightedRect)
            screen.blit(textbox2, textbox2Rect)
        if textboxSelected == 2:
            screen.blit(textboxHighlighted2, textboxHighlighted2Rect)
            screen.blit(textbox, textboxRect)
            
        mpos = pygame.mouse.get_pos()
        #checks to see if the user quits
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_mouse_selection(textboxRect,mpos):
                    textboxSelected = 1
                elif is_mouse_selection(textbox2Rect,mpos):
                    textboxSelected = 2
                
                    
                if is_mouse_selection(playButtonRect,mpos):
                    play_game(player1name,player2name)
                    return
                elif easySelected==1 and is_mouse_selection(checkbox2Rect,mpos):
                    easySelected=0
                elif easySelected==0 and is_mouse_selection(checkboxRect,mpos):
                    easySelected=1
                    
            if event.type == KEYDOWN:
                if textboxSelected == 1:
                    player1name = check_keys(player1name, event.key)
                elif textboxSelected == 2:
                    player2name = check_keys(player2name,event.key)
                    
                    
        
        screen.blit(player1name_label,player1name_rect)
        screen.blit(player2name_label,player2name_rect)
        pygame.display.flip()