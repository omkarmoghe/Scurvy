import main
from Globals import *
from ControlBox import *


def show_customization():

    pygame.display.set_caption('Customization Menu')

    quit_status = 0
    easy_selected = 1

    textbox_selected = 0

    player1name = 'PLAYER 1'
    player2name = 'PLAYER 2'

    menu_background = pygame.image.load(menu_background_image)
    menu_background_rect = menu_background.get_rect()

    title_label = pygame.font.Font(font_file, 70).render('{0}'.format('Customization'), True, WHITE)
    title_rect = title_label.get_rect()
    title_rect.centerx = WIDTH * 1 / 2
    title_rect.centery = HEIGHT * 1 / 5

    # creates the difficulty label
    difficulty_label = pygame.font.Font(font_file, 50).render('{0}'.format('Difficulty'), True, WHITE)
    difficulty_rect = difficulty_label.get_rect()
    difficulty_rect.centerx = WIDTH * 1 / 4
    difficulty_rect.centery = HEIGHT * 2 / 5

    # creates the sound on label
    easy_label = pygame.font.Font(font_file, 30).render('{0}'.format('Easy'), True, WHITE)
    easy_rect = easy_label.get_rect()
    easy_rect.centerx = WIDTH * 1 / 5
    easy_rect.centery = HEIGHT * 3 / 5

    # creates the sound off label
    hard_label = pygame.font.Font(font_file, 30).render('{0}'.format('Hard'), True, WHITE)
    hard_rect = hard_label.get_rect()
    hard_rect.centerx = WIDTH * 1 / 5
    hard_rect.centery = HEIGHT * 5 / 7

    # creates the names label
    names_label = pygame.font.Font(font_file, 50).render('{0}'.format('Names'), True, WHITE)
    names_rect = names_label.get_rect()
    names_rect.centerx = WIDTH * 3 / 4
    names_rect.centery = HEIGHT * 2 / 5

    # creates the player 1 label
    player1_label = pygame.font.Font(font_file, 30).render('{0}'.format('Player 1'), True, WHITE)
    player1_rect = player1_label.get_rect()
    player1_rect.centerx = WIDTH * 3 / 5
    player1_rect.centery = HEIGHT * 3 / 5

    # creates the player 2 label
    player2_label = pygame.font.Font(font_file, 30).render('{0}'.format('Player 2'), True, WHITE)
    player2_rect = player2_label.get_rect()
    player2_rect.centerx = WIDTH * 3 / 5
    player2_rect.centery = HEIGHT * 5 / 7

    # creates the unchecked on box, image from iconfinder.com from visual pharm
    checkbox = ControlBox(checkbox_image, checkbox_selected_image, (WIDTH / 3, HEIGHT * 3 / 5),
                          (checkbox_size, checkbox_size), True)
    checkbox2 = ControlBox(checkbox_image, checkbox_selected_image, (WIDTH / 3, HEIGHT * 5 / 7),
                           (checkbox_size, checkbox_size))
    '''checkbox = pygame.image.load(checkbox_image)
    checkbox = pygame.transform.scale(checkbox, (checkbox_size, checkbox_size))
    checkbox_rect = checkbox.get_rect()
    checkbox_rect.centerx = WIDTH * 1 / 3
    checkbox_rect.centery = HEIGHT * 3 / 5
    checkbox_rect.left = checkbox_rect.centerx - (checkbox_size / 2)
    checkbox_rect.right = checkbox_rect.centerx + (checkbox_size / 2)
    checkbox_rect.top = checkbox_rect.centery - (checkbox_size / 2)
    checkbox_rect.bottom = checkbox_rect.centery + (checkbox_size / 2)

    # creates the unchecked off box, image from iconfinder.com from visual pharm
    checkbox2 = pygame.image.load(checkbox_image)
    checkbox2 = pygame.transform.scale(checkbox2, (checkbox_size, checkbox_size))
    checkbox2rect = checkbox2.get_rect()
    checkbox2rect.centerx = WIDTH * 1 / 3
    checkbox2rect.centery = HEIGHT * 5 / 7
    checkbox2rect.left = checkbox2rect.centerx - (checkbox_size / 2)
    checkbox2rect.right = checkbox2rect.centerx + (checkbox_size / 2)
    checkbox2rect.top = checkbox2rect.centery - (checkbox_size / 2)
    checkbox2rect.bottom = checkbox2rect.centery + (checkbox_size / 2)

    # creates the checked on box, image from iconfinder.com from visual pharm, icons8.com
    checkbox_selected = pygame.image.load(checkbox_selected_image)
    checkbox_selected = pygame.transform.scale(checkbox_selected, (checkbox_size, checkbox_size))
    checkbox_selected_rect = checkbox_selected.get_rect()
    checkbox_selected_rect.centerx = WIDTH * 1 / 3
    checkbox_selected_rect.centery = HEIGHT * 3 / 5
    checkbox_selected_rect.left = checkbox_selected_rect.centerx - (checkbox_size / 2)
    checkbox_selected_rect.right = checkbox_selected_rect.centerx + (checkbox_size / 2)
    checkbox_selected_rect.top = checkbox_selected_rect.centery - (checkbox_size / 2)
    checkbox_selected_rect.bottom = checkbox_selected_rect.centery + (checkbox_size / 2)

    # creates the checked off box, image from iconfinder.com from visual pharm
    checkbox_selected2 = pygame.image.load(checkbox_selected_image)
    checkbox_selected2 = pygame.transform.scale(checkbox_selected2, (checkbox_size, checkbox_size))
    checkbox_selected2rect = checkbox_selected2.get_rect()
    checkbox_selected2rect.centerx = WIDTH * 1 / 3
    checkbox_selected2rect.centery = HEIGHT * 5 / 7
    checkbox_selected2rect.left = checkbox_selected2rect.centerx - (checkbox_size / 2)
    checkbox_selected2rect.right = checkbox_selected2rect.centerx + (checkbox_size / 2)
    checkbox_selected2rect.top = checkbox_selected2rect.centery - (checkbox_size / 2)
    checkbox_selected2rect.bottom = checkbox_selected2rect.centery + (checkbox_size / 2)'''
    '''textbox = pygame.image.load(textbox_image)
    textbox_rect = textbox.get_rect()
    textbox_rect.centerx = WIDTH * 6 / 7
    textbox_rect.centery = HEIGHT * 3 / 5
    # textbox_rect.left = textbox_rect.centerx - 110
    # textbox_rect.right = textbox_rect.centerx + 110
    # textbox_rect.top = textbox_rect.centery - 30
    # textbox_rect.bottom = textbox_rect.centery + 30

    # creates the player 2 box
    textbox2 = pygame.image.load(textbox_image)
    textbox2rect = textbox2.get_rect()
    textbox2rect.centerx = WIDTH * 6 / 7
    textbox2rect.centery = HEIGHT * 5 / 7
    # textbox2rect.left = textbox2rect.centerx - 110
    # textbox2rect.right = textbox2rect.centerx + 110
    # textbox2rect.top = textbox2rect.centery - 30
    # textbox2rect.bottom = textbox2rect.centery + 30

    # creates the player 1 highlighted box
    textbox_highlighted = pygame.image.load(textbox_highlighted_image)
    textbox_highlighted_rect = textbox_highlighted.get_rect()
    textbox_highlighted_rect.centerx = WIDTH * 6 / 7
    textbox_highlighted_rect.centery = HEIGHT * 3 / 5
    # textbox_highlighted_rect.left = textbox_highlighted_rect.centerx - 110
    # textbox_highlighted_rect.right = textbox_highlighted_rect.centerx + 110
    # textbox_highlighted_rect.top = textbox_highlighted_rect.centery - 30
    # textbox_highlighted_rect.bottom = textbox_highlighted_rect.centery + 30

    # creates the player 2 highlighted box
    textbox_highlighted2 = pygame.image.load(textbox_highlighted_image)
    textbox_highlighted2rect = textbox_highlighted2.get_rect()
    textbox_highlighted2rect.centerx = WIDTH * 6 / 7
    textbox_highlighted2rect.centery = HEIGHT * 5 / 7
    # textbox_highlighted2rect.left = textbox_highlighted2rect.centerx - 110
    # textbox_highlighted2rect.right = textbox_highlighted2rect.centerx + 110
    # textbox_highlighted2rect.top = textbox_highlighted2rect.centery - 30
    # textbox_highlighted2rect.bottom = textbox_highlighted2rect.centery + 30'''

    '''play_button = pygame.image.load(play_button_image)
    play_button = pygame.transform.scale(play_button, (60, 60))
    play_button_rect = play_button.get_rect()
    play_button_rect.centerx = WIDTH * 1 / 2
    play_button_rect.centery = HEIGHT * 14 / 15
    # play_button_rect.left = play_button_rect.centerx - 30
    # play_button_rect.right = play_button_rect.centerx + 30
    # play_button_rect.top = play_button_rect.centery - 30
    # play_button_rect.bottom = play_button_rect.centery + 30

    back_button = pygame.image.load(back_button_image)
    back_button = pygame.transform.scale(back_button, (60, 60))
    back_button_rect = back_button.get_rect()
    back_button_rect.centerx = 50
    back_button_rect.centery = 50
    # back_button_rect.left = back_button_rect.centerx - 30
    # back_button_rect.right = back_button_rect.centerx + 30
    # back_button_rect.top = back_button_rect.centery - 30
    # back_button_rect.bottom = back_button_rect.centery + 30'''

    # creates the player 1 box
    textbox = ControlBox(textbox_image, textbox_highlighted_image, (WIDTH * 6 / 7, HEIGHT * 3 / 5), None)
    textbox2 = ControlBox(textbox_image, textbox_highlighted_image, (WIDTH * 6 / 7, HEIGHT * 5 / 7), None)

    # creates the play label
    play_label = pygame.font.Font(font_file, 50).render('{0}'.format('Play!'), True, WHITE)
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

            if event.type == pygame.MOUSEBUTTONDOWN:
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
                    infile = open("sound_and_cheat.txt", "r")
                    array = infile.readlines()
                    if player1name == "":
                        player1name = "PLAYER 1"
                    if player2name == "":
                        player2name = "PLAYER 2"
                    main.play_game(player1name, player2name, easy_selected, array[0], array[1])
                    return
                elif easy_selected == 1 and checkbox2.is_mouse_selection(m_pos):
                    easy_selected = 0
                    checkbox.selected = False
                elif easy_selected == 0 and checkbox.is_mouse_selection(m_pos):
                    easy_selected = 1
                    checkbox2.selected = False
            if event.type == KEYDOWN:
                if textbox_selected == 1:
                    player1name = check_keys(player1name, event.key)
                elif textbox_selected == 2:
                    player2name = check_keys(player2name, event.key)

        screen.blit(title_label, title_rect)
        screen.blit(difficulty_label, difficulty_rect)
        screen.blit(easy_label, easy_rect)
        screen.blit(hard_label, hard_rect)

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
        player1name_label = pygame.font.Font(font_file, 25).render('{0}'.format(player1name), True, BLACK)
        player1name_rect = player1name_label.get_rect()
        player1name_rect.left = WIDTH * 5 / 7 + 10
        player1name_rect.centery = HEIGHT * 3 / 5

        # creates the player 2 name label
        player2name_label = pygame.font.Font(font_file, 25).render('{0}'.format(player2name), True, BLACK)
        player2name_rect = player2name_label.get_rect()
        player2name_rect.left = WIDTH * 5 / 7 + 10
        player2name_rect.centery = HEIGHT * 5 / 7

        screen.blit(player1name_label, player1name_rect)
        screen.blit(player2name_label, player2name_rect)
        pygame.display.flip()