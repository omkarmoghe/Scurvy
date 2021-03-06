import main
from Globals import *
from ControlBox import *


def show_customization():

    pygame.display.set_caption('Customization Menu')

    quit_status = 0
    easy_selected = 1
    ship_location = classic_ship_location

    textbox_selected = 0

    player1name = 'PLAYER 1'
    player2name = 'PLAYER 2'

    menu_background = pygame.image.load(menu_background_image)
    menu_background_rect = menu_background.get_rect()

    title_label = pygame.font.Font(menu_font, 70).render('{0}'.format('Customization'), True, WHITE)
    title_rect = title_label.get_rect()
    title_rect.centerx = WIDTH * 1 / 2
    title_rect.centery = HEIGHT * 1 / 6

    # creates the difficulty label
    difficulty_label = pygame.font.Font(menu_font, 40).render('{0}'.format('Difficulty'), True, WHITE)
    difficulty_rect = difficulty_label.get_rect()
    difficulty_rect.centerx = WIDTH * 1 / 6
    difficulty_rect.centery = HEIGHT * 1 / 3

    # creates the sound on label
    easy_label = pygame.font.Font(menu_font, 30).render('{0}'.format('Easy'), True, WHITE)
    easy_rect = easy_label.get_rect()
    easy_rect.centerx = WIDTH * 1 / 10
    easy_rect.centery = HEIGHT * 5 / 9

    # creates the sound off label
    hard_label = pygame.font.Font(menu_font, 30).render('{0}'.format('Hard'), True, WHITE)
    hard_rect = hard_label.get_rect()
    hard_rect.centerx = WIDTH * 1 / 10
    hard_rect.centery = HEIGHT * 5 / 7
    
    # creates the ship label
    ship_label = pygame.font.Font(menu_font, 40).render('{0}'.format('Ship'), True, WHITE)
    ship_rect = ship_label.get_rect()
    ship_rect.centerx = WIDTH * 1 / 2
    ship_rect.centery = HEIGHT * 1 / 3

    angle_for_ship = "/PlayerShip0.0.png"

    classic_boat_image = classic_ship_location + angle_for_ship
    classic_boat = pygame.image.load(classic_boat_image)
    classic_boat = pygame.transform.scale(classic_boat, (menu_ship_scale, menu_ship_scale))
    classic_boat_rect = classic_boat.get_rect()
    classic_boat_rect.centerx = WIDTH * 1/2
    classic_boat_rect.centery = HEIGHT * 4 / 9 + 10
    
    michigan_boat_image = maize_and_blue_ship_location + angle_for_ship
    michigan_boat = pygame.image.load(michigan_boat_image)
    michigan_boat = pygame.transform.scale(michigan_boat, (menu_ship_scale, menu_ship_scale))
    michigan_boat_rect = michigan_boat.get_rect()
    michigan_boat_rect.centerx = WIDTH * 1 / 2
    michigan_boat_rect.centery = HEIGHT * 5 / 9 + 10
    
    neon_boat_image = neon_ship_location + angle_for_ship
    neon_boat = pygame.image.load(neon_boat_image)
    neon_boat = pygame.transform.scale(neon_boat, (menu_ship_scale, menu_ship_scale))
    neon_boat_rect = neon_boat.get_rect()
    neon_boat_rect.centerx = WIDTH * 1 / 2
    neon_boat_rect.centery = HEIGHT * 2 / 3 + 10
    
    ship_checkbox1 = ControlBox(checkbox_image, checkbox_selected_image, (WIDTH * 13 / 20, HEIGHT * 4 / 9 + 10),
                                (checkbox_size, checkbox_size), True)
    ship_checkbox2 = ControlBox(checkbox_image, checkbox_selected_image, (WIDTH * 13 / 20, HEIGHT * 5 / 9 + 10),
                                (checkbox_size, checkbox_size))
    ship_checkbox3 = ControlBox(checkbox_image, checkbox_selected_image, (WIDTH * 13 / 20, HEIGHT * 6 / 9 + 10),
                                (checkbox_size, checkbox_size))

    # creates the names label
    names_label = pygame.font.Font(menu_font, 40).render('{0}'.format('Names'), True, WHITE)
    names_rect = names_label.get_rect()
    names_rect.centerx = WIDTH * 6 / 7
    names_rect.centery = HEIGHT * 1 / 3

    # creates the player 1 label
    player1_label = pygame.font.Font(menu_font, 20).render('{0}'.format('Player 1'), True, WHITE)
    player1_rect = player1_label.get_rect()
    player1_rect.centerx = WIDTH * 12 / 14
    player1_rect.centery = HEIGHT * 1 / 2

    # creates the player 2 label
    player2_label = pygame.font.Font(menu_font, 20).render('{0}'.format('Player 2'), True, WHITE)
    player2_rect = player2_label.get_rect()
    player2_rect.centerx = WIDTH * 12 / 14
    player2_rect.centery = HEIGHT * 9 / 14 + 10

    checkbox = ControlBox(checkbox_image, checkbox_selected_image, (WIDTH / 4, HEIGHT * 5 / 9),
                          (checkbox_size, checkbox_size), True)
    checkbox2 = ControlBox(checkbox_image, checkbox_selected_image, (WIDTH / 4, HEIGHT * 5 / 7),
                           (checkbox_size, checkbox_size))

    # creates the player 1 box
    textbox = ControlBox(textbox_image, textbox_highlighted_image, (WIDTH * 12 / 14, HEIGHT * 5 / 9),
                         (textbox_width, textbox_height))
    textbox2 = ControlBox(textbox_image, textbox_highlighted_image, (WIDTH * 12 / 14, HEIGHT * 5 / 7),
                          (textbox_width, textbox_height))

    # creates the play label
    play_label = pygame.font.Font(menu_font, 50).render('{0}'.format('Play!'), True, WHITE)
    play_rect = play_label.get_rect()
    play_rect.centerx = WIDTH * 1 / 2
    play_rect.centery = HEIGHT * 5 / 6

    play_button = ControlBox(play_button_image, None, (WIDTH / 2, HEIGHT * 14 / 15), (button_size, button_size))
    back_button = ControlBox(back_button_image, None, (50, 50), (button_size, button_size))

    while quit_status != 1:
        screen.blit(menu_background, menu_background_rect)

        m_pos = pygame.mouse.get_pos()
        # checks to see if the user quits
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            if event.type == KEYDOWN and (event.key == K_TAB):
                if textbox_selected == 1:
                    if player1name == "":
                        player1name = "PLAYER 1"
                    textbox_selected = 2
                    textbox.selected = False
                    textbox2.selected = True
                    if player2name == "PLAYER 2":
                        player2name = ""
                elif textbox_selected == 2:
                    if player1name == "PLAYER 1":
                        player1name = ""
                    textbox_selected = 1
                    textbox.selected = True
                    textbox2.selected = False
                    if player2name == "":
                        player2name = "PLAYER 2"

            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                if back_button.is_mouse_selection(m_pos):
                    return
                if textbox.is_mouse_selection(m_pos):
                    textbox_selected = 1
                    textbox2.selected = False
                    if player2name == "":
                        player2name = "PLAYER 2"
                    if player1name == "PLAYER 1":
                        player1name = ""

                elif textbox2.is_mouse_selection(m_pos):
                    textbox.selected = False
                    if player1name == "":
                        player1name = "PLAYER 1"
                    if player2name == "PLAYER 2":
                        player2name = ""
                    textbox_selected = 2

                if play_button.is_mouse_selection(m_pos):
                    infile = open(settings_file, "r")
                    array = infile.readlines()
                    if player1name == "":
                        player1name = "PLAYER 1"
                    if player2name == "":
                        player2name = "PLAYER 2"
                    main.play_game(player1name, player2name, easy_selected, array[0], array[1], array[2], ship_location)
                    return
                elif easy_selected == 1 and checkbox2.is_mouse_selection(m_pos):
                    easy_selected = 0
                    checkbox.selected = False
                elif easy_selected == 0 and checkbox.is_mouse_selection(m_pos):
                    easy_selected = 1
                    checkbox2.selected = False
                elif ship_checkbox1.is_mouse_selection(m_pos):
                    ship_checkbox1.selected = True
                    ship_checkbox2.selected = False
                    ship_checkbox3.selected = False
                    ship_location = classic_ship_location
                elif ship_checkbox2.is_mouse_selection(m_pos):
                    ship_checkbox2.selected = True
                    ship_checkbox1.selected = False
                    ship_checkbox3.selected = False
                    ship_location = maize_and_blue_ship_location
                elif ship_checkbox3.is_mouse_selection(m_pos):
                    ship_checkbox3.selected = True
                    ship_checkbox2.selected = False
                    ship_checkbox1.selected = False
                    ship_location = neon_ship_location
            if event.type == KEYDOWN:
                if textbox_selected == 1:
                    player1name = check_keys(player1name, event.key)
                elif textbox_selected == 2:
                    player2name = check_keys(player2name, event.key)

        screen.blit(title_label, title_rect)
        screen.blit(difficulty_label, difficulty_rect)
        screen.blit(easy_label, easy_rect)
        screen.blit(hard_label, hard_rect)
        
        screen.blit(ship_label, ship_rect)
        screen.blit(classic_boat, classic_boat_rect)
        screen.blit(michigan_boat, michigan_boat_rect)
        screen.blit(neon_boat, neon_boat_rect)
        screen.blit(ship_checkbox1.get_image(), ship_checkbox1.rect)
        screen.blit(ship_checkbox2.get_image(), ship_checkbox2.rect)
        screen.blit(ship_checkbox3.get_image(), ship_checkbox3.rect)

        screen.blit(names_label, names_rect)
        screen.blit(player1_label, player1_rect)
        screen.blit(player2_label, player2_rect)

        screen.blit(play_label, play_rect)
        screen.blit(play_button.image, play_button.rect)
        screen.blit(back_button.image, back_button.rect)

        screen.blit(checkbox.get_image(), checkbox.rect)
        screen.blit(checkbox2.get_image(), checkbox2.rect)
        screen.blit(textbox.get_image(), textbox.rect)
        screen.blit(textbox2.get_image(), textbox2.rect)

        # creates the player 1 name label
        player1name_label = pygame.font.Font(menu_font, 18).render('{0}'.format(player1name), True, BLACK)
        player1name_rect = player1name_label.get_rect()
        player1name_rect.left = WIDTH * 10/13 + 5
        player1name_rect.centery = HEIGHT * 5 / 9

        # creates the player 2 name label
        player2name_label = pygame.font.Font(menu_font, 18).render('{0}'.format(player2name), True, BLACK)
        player2name_rect = player2name_label.get_rect()
        player2name_rect.left = WIDTH * 10/13 + 5
        player2name_rect.centery = HEIGHT * 5 / 7

        screen.blit(player1name_label, player1name_rect)
        screen.blit(player2name_label, player2name_rect)
        pygame.display.flip()