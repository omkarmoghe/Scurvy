from Globals import *

tf = open(settings_file, 'w')
tf.write("%s\n%s\n" % ("On", ""))  # TODO: Fix resetting preferences every single time.
tf.close()


# This represents a selectable item in the menu.
class MenuItem(pygame.font.Font):

    def __init__(self, text, index, count, func):
 
        pygame.font.Font.__init__(self, menu_font, menu_item_font_size)
        self.text = text
        self.font_size = menu_item_font_size
        self.font_color = WHITE
        self.label = self.render(self.text, True, self.font_color)
        self.rect = self.label.get_rect()
        pos_x = (WIDTH / 2) - (self.rect.width / 2)
        pos_y = 200 + ((HEIGHT - 220) / count) * index
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.func = func
 
    def is_mouse_selection(self, (pos_x, pos_y)):
        return self.rect.collidepoint(pos_x, pos_y)
 
    def set_selected(self, selected):
        if selected:
            self.font_color = BLACK
        else:
            self.font_color = WHITE
        self.label = self.render(self.text, True, self.font_color)


class GameMenu():
    def __init__(self, items):

        self.bg_color = BLACK
        self.clock = pygame.time.Clock()
        self.items = []
        count = len(items)
        for index, item in enumerate(items):
            menu_item = MenuItem(item, index, count, items[item])
            self.items.append(menu_item)
        self.mouse_is_visible = True
        self.cur_item = None
 
    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)
 
    def set_keyboard_selection(self, key):
        for item in self.items:
            # Return all to neutral
            item.set_selected(False)
 
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

        self.items[self.cur_item].set_selected(True)
 
        # Finally check if Enter or Space is pressed
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            pygame.mouse.set_visible(True)
            self.items[self.cur_item].func()
            pygame.display.set_caption(application_name)
        # If escape, quit.
        if key == pygame.K_ESCAPE:
            quit()

    def run(self):
        mainloop = True
        menu_background = pygame.image.load(menu_background_image)
        menu_background_rect = menu_background.get_rect()

        title_label = pygame.font.Font(menu_font, 100).render('{0}'.format(application_name), True, WHITE)
        title_rect = title_label.get_rect()
        title_rect.centerx = WIDTH * 1 / 2
        title_rect.centery = HEIGHT * 1 / 5

        boat_image = classic_ship_location + "PlayerShip337.5.png"  # TODO: Make boat animation
        boat = pygame.image.load(boat_image)
        boat = pygame.transform.scale(boat, (menu_ship_scale, menu_ship_scale))
        boat_rect = boat.get_rect()
        boat_rect.centerx = WIDTH * 4 / 5
        boat_rect.centery = HEIGHT * 2 / 5

        while mainloop:

            m_pos = pygame.mouse.get_pos()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_keyboard_selection(event.key)
                if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                    for item in self.items:
                        if item.is_mouse_selection(m_pos):
                            item.func()
                            pygame.display.set_caption(application_name)
 
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None
 
            self.set_mouse_visibility()
 
            # Redraw the background
            screen.blit(menu_background, menu_background_rect)
            screen.blit(title_label, title_rect)
            screen.blit(boat, boat_rect)

            for item in self.items:
                if self.mouse_is_visible:
                    set_mouse_selection(item, m_pos)
                screen.blit(item.label, item.rect)
            pygame.display.flip()


def set_mouse_selection(item, m_pos):
    """Marks the MenuItem the mouse cursor hovers on."""
    if item.is_mouse_selection(m_pos):
        item.set_selected(True)
    else:
        item.set_selected(False)
        # item.set_italic(False)