from Globals import *
from ControlBox import *


def show_credits():
    quit_status = 0
    pygame.display.set_caption('Credits')

    menu_background = pygame.image.load(menu_background_image)
    menu_background_rect = menu_background.get_rect()

    title_label = pygame.font.Font(font_file, 70).render('{0}'.format('Credits'), True, WHITE)
    title_rect = title_label.get_rect()
    title_rect.centerx = WIDTH * 1 / 2
    title_rect.centery = HEIGHT * 1 / 5

    infile = open(credits_file, "r")
    array = infile.readlines()
    credit_labels = []
    for (i, credit) in enumerate(array):
        credit = credit[:len(credit)-1]
        credit_label = pygame.font.Font(font_file, 15).render('{0}'.format(credit), True, WHITE)
        credit_label_rect = credit_label.get_rect()
        credit_label_rect.left = WIDTH * 1/10
        credit_label_rect.centery = HEIGHT * 2/5 + i * 20
        credit_labels.append((credit_label, credit_label_rect))

    back_button = ControlBox(back_button_image, None, (50, 50), (button_size, button_size))

    while quit_status != 1:
        screen.blit(menu_background, menu_background_rect)

        screen.blit(title_label, title_rect)
        
        for credit in credit_labels:
            screen.blit(credit[0], credit[1])

        screen.blit(back_button.image, back_button.rect)
        
        m_pos = pygame.mouse.get_pos()
        # checks to see if the user quits
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                if back_button.is_mouse_selection(m_pos):
                    return
        pygame.display.flip()