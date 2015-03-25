#https://nebelprog.wordpress.com/2013/09/02/create-a-simple-game-menu-with-pygame-pt-4-connecting-it-to-functions/

import sys
import pygame
from main import *
from CreditsMenu import *
from SettingsMenu import *
from CustomizationMenu import *

pygame.init()
 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
 
class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=50,
                 font_color=WHITE, (pos_x, pos_y)=(0, 0)):
 
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width + font_size
        self.height = self.label.get_rect().height + font_size/2
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
 
    def is_mouse_selection(self, (posx, posy)):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
           (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False
 
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)


class GameMenu():
    def __init__(self, screen, items, funcs, bg_color=BLACK, font=None, font_size=50,
                 font_color=WHITE):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
        self.funcs = funcs
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)
 
            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            # This line includes a bug fix by Ariel (Thanks!)
            # Please check the comments section of pt. 2 for an explanation
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index*2) + index * menu_item.height)
 
            menu_item.set_position(pos_x*14/15, pos_y*5/4)
            self.items.append(menu_item)
 
        self.mouse_is_visible = True
        self.cur_item = None
 
    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)
 
    def set_keyboard_selection(self, key):
        """
        Marks the MenuItem chosen via up and down keys.
        """
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(WHITE)
 
        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Find the chosen item
            if key == pygame.K_UP and \
                    self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_UP and \
                    self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_DOWN and \
                    self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pygame.K_DOWN and \
                    self.cur_item == len(self.items) - 1:
                self.cur_item = 0
 
        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(BLACK)
 
        # Finally check if Enter or Space is pressed
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            text = self.items[self.cur_item].text
            pygame.mouse.set_visible(True)
            self.funcs[text]()
 
    def set_mouse_selection(self, item, mpos):
        """Marks the MenuItem the mouse cursor hovers on."""
        if item.is_mouse_selection(mpos):
            item.set_font_color(BLACK)
            item.set_italic(True)
        else:
            item.set_font_color(WHITE)
            item.set_italic(False)
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
            mpos = pygame.mouse.get_pos()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_keyboard_selection(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.items:
                        if item.is_mouse_selection(mpos):
                            self.funcs[item.text]()
 
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None
 
            self.set_mouse_visibility()
 
            # Redraw the background
            background_image = "Resources/MenuBackground.png" 
            background = pygame.image.load(background_image)
            backgroundRect = background.get_rect()
            self.screen.blit(background,backgroundRect)
            
            title_label = pygame.font.Font(font_file, 100).render('{0}'.format('Scurvy'),
                                                                       True, (255, 255, 255))
            title_rect = title_label.get_rect()
            title_rect.centerx = self.scr_width * 1 / 2
            title_rect.centery = self.scr_height * 1 / 5
            self.screen.blit(title_label, title_rect)
            
            boat_image = "Resources/MenuShip.png"
            boat = pygame.image.load(boat_image)
            boat = pygame.transform.scale(boat,(200,200))
            boatRect = boat.get_rect()
            boatRect.centerx = self.scr_width * 4 / 5
            boatRect.centery = self.scr_height * 2 / 5
            self.screen.blit(boat, boatRect)
        
 
            for item in self.items:
                if self.mouse_is_visible:
                    self.set_mouse_selection(item, mpos)
                itemlabel = pygame.font.Font(font_file, item.font_size).render('{0}'.format(item.text),
                                                                       True, (item.font_color))
                self.screen.blit(itemlabel, item.position)
 
            pygame.display.flip()
 
if __name__ == "__main__":
    def hello_world():
        print "Start!"
    def hello_world2():
        print "Settings!"
    def hello_world3():
        print "Credits!"
    # Creating the screen
    pygame.display.set_caption("Scurvy")
    background_image = "Resources/Background.png" 
    background = pygame.image.load(background_image)
    backgroundRect = background.get_rect()
    WIDTH = backgroundRect.width
    HEIGHT = 3 * backgroundRect.height / 2
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    menu_items = ('Start', 'Settings', 'Quit', 'Credits')
    funcs = {'Start': show_Customization,
             'Quit': sys.exit,
             'Settings': show_Settings,
             'Credits': show_Credits
             }
 
    gm = GameMenu(screen, funcs.keys(), funcs)
    gm.run()