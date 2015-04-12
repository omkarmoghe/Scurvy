from ControlBox import *
from Globals import *
from pygame.locals import *


def quit_settings(on_selected, cheat):
    settings_file_io = open(settings_file, 'w')
    if on_selected == 0:
        on_selected = sound_on_string
    else:
        on_selected = sound_off_string
    if cheat == "" or not all_codes.__contains__(cheat):
        cheat = "\n"
    settings_file_io.write("%s\n%s" % (on_selected, cheat))
    settings_file_io.close()


def show_settings():
    quit_status = 0
    on_selected = 0
    textbox_selected = 0
    cheat = ''
    menu_background = pygame.image.load(menu_background_image)
    menu_background_rect = menu_background.get_rect()

    # creates the label at the top
    title_label = pygame.font.Font(menu_font, 70).render('{0}'.format('Settings'), True, WHITE)
    title_rect = title_label.get_rect()
    title_rect.centerx = WIDTH * 1 / 2
    title_rect.centery = HEIGHT * 1 / 5

    # creates the sound label
    sound_label = pygame.font.Font(menu_font, 50).render('{0}'.format('Sound'), True, WHITE)
    sound_rect = sound_label.get_rect()
    sound_rect.centerx = WIDTH * 1 / 4
    sound_rect.centery = HEIGHT * 2 / 5

    # creates the sound on label
    sound_on_label = pygame.font.Font(menu_font, 30).render('{0}'.format('On'), True, WHITE)
    sound_on_rect = sound_on_label.get_rect()
    sound_on_rect.centerx = WIDTH * 1 / 4
    sound_on_rect.centery = HEIGHT * 3 / 5

    # creates the sound off label
    sound_off_label = pygame.font.Font(menu_font, 30).render('{0}'.format('Off'), True, WHITE)
    sound_off_rect = sound_off_label.get_rect()
    sound_off_rect.centerx = WIDTH * 1 / 4
    sound_off_rect.centery = HEIGHT * 5 / 7

    # creates the cheats label
    cheats_label = pygame.font.Font(menu_font, 50).render('{0}'.format('Cheats'), True, WHITE)
    cheats_rect = cheats_label.get_rect()
    cheats_rect.centerx = WIDTH * 3 / 4
    cheats_rect.centery = HEIGHT * 2 / 5

    sound_on_checkbox = ControlBox(checkbox_image, checkbox_selected_image, (WIDTH / 3, HEIGHT * 3 / 5),
                                   (checkbox_size, checkbox_size), True)
    sound_off_checkbox = ControlBox(checkbox_image, checkbox_selected_image, (WIDTH / 3, HEIGHT * 5 / 7),
                                    (checkbox_size, checkbox_size))

    textbox = ControlBox(textbox_image, textbox_highlighted_image, (WIDTH * 3 / 4, HEIGHT * 3 / 5), None)

    back_button = ControlBox(back_button_image, None, (50, 50), (button_size, button_size))
    settings_file_io = open(settings_file, "r")
    preferences = settings_file_io.read().split("\n")
    if len(preferences) > 0:
        if preferences[0] == sound_off_string:
            on_selected = 1
            sound_off_checkbox.selected = True
            sound_on_checkbox.selected = False
        elif preferences[0] == sound_on_string:
            on_selected = 0
            sound_off_checkbox.selected = False
            sound_on_checkbox.selected = True
        else:
            print "Fatal error: Sound preferences could not be read."
    if len(preferences) > 1:
        if all_codes.__contains__(preferences[1]):
            cheat = preferences[1]

    while quit_status != 1:
    
        pygame.display.set_caption('Settings')

        screen.blit(menu_background, menu_background_rect)

        screen.blit(title_label, title_rect)
        screen.blit(sound_label, sound_rect)
        screen.blit(sound_on_label, sound_on_rect)
        screen.blit(sound_off_label, sound_off_rect)
        screen.blit(cheats_label, cheats_rect)
        
        cheats_name_label = pygame.font.Font(menu_font, 25).render('{0}'.format(cheat), True, BLACK)
        cheats_name_rect = cheats_name_label.get_rect()
        cheats_name_rect.left = WIDTH * 3 / 5 + 15
        cheats_name_rect.centery = HEIGHT * 3 / 5

        screen.blit(back_button.image, back_button.rect)

        screen.blit(sound_on_checkbox.get_image(), sound_on_checkbox.rect)
        screen.blit(sound_off_checkbox.get_image(), sound_off_checkbox.rect)
        screen.blit(textbox.get_image(), textbox.rect)

        m_pos = pygame.mouse.get_pos()
        # checks to see if the user quits
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                quit_settings(on_selected, cheat)
                quit_status = 1
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                if back_button.is_mouse_selection(m_pos):
                    quit_settings(on_selected, cheat)
                    quit_status = 1
                if textbox.is_mouse_selection(m_pos):
                    textbox_selected = 1
                if on_selected == 1 and sound_on_checkbox.is_mouse_selection(m_pos):
                    on_selected = 0
                    sound_off_checkbox.selected = False
                elif on_selected == 0 and sound_off_checkbox.is_mouse_selection(m_pos):
                    on_selected = 1
                    sound_on_checkbox.selected = False
            
            if event.type == KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if not all_codes.__contains__(cheat):
                        cheat = ''
                    else:
                        textbox_selected = 0
                        textbox.selected = False
                if textbox_selected == 1:
                    cheat = check_keys(cheat, event.key)

        screen.blit(cheats_name_label, cheats_name_rect)
        pygame.display.flip()