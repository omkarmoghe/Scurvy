import os
from ControlBox import *
import main
from Globals import *


# HIGH SCORES FORMAT IS AS FOLLOWS:
#     Player1:Player2:score
# ex. Bart:Lisa:400
class HighScoreManager():

    def __init__(self, filename):
        self.filename = filename
        self.high_scores = self.load_high_scores()
        self.sort_high_scores()

    def load_high_scores(self):
        if not os.path.isfile(self.filename):
            f_out = open(self.filename, 'w')
            f_out.close()

        high_scores = []

        f_in = open(self.filename, 'r')
        for line in f_in:
            score_set = line.split(':')  # split the line at the colon
            high_scores.append((score_set[0], score_set[1], int(score_set[2])))  # first part is name, second is score

        f_in.close()

        return high_scores

    def save_high_scores(self):
        self.sort_high_scores()

        f_out = open(self.filename, 'w')

        for pair in self.high_scores:
            f_out.write(pair[0] + ':' + pair[1] + ':' + str(pair[2]) + '\n')

        f_out.close()

    def sort_high_scores(self):
        self.high_scores.sort(key=lambda tup: tup[2])
        self.high_scores.reverse()

    # set is a tuple (Player1, Player2, score)
    def add_high_score(self, score_set):
        if len(self.high_scores) < 10:
            self.sort_high_scores()
            self.high_scores.append(score_set)
            self.sort_high_scores()
            self.save_high_scores()
        elif len(self.high_scores) == 10:
            self.high_scores.append(score_set)
            self.sort_high_scores()
            del self.high_scores[-1]
            self.save_high_scores()
        else:
            assert False  # should never be the case

    def draw(self, p1name, p2name, easy_selected, ship_location):
        running = True

        menu_background = pygame.image.load(menu_background_image)
        menu_background_rect = menu_background.get_rect()

        position_label = pygame.font.Font(menu_font, 25).render('High Scores Table', True, (255, 255, 255))
        position_label_rect = position_label.get_rect()
        position_label_rect.centerx = WIDTH / 2

        ratio = HEIGHT / 12
        position_label_rect.centery = int(ratio)
        score_labels = []
        for (i, score) in enumerate(self.high_scores):
            score_label = pygame.font.Font(menu_font, 20).render('{0:12s} {1:12s} scored {2:10d} points.'.format
                                                                 (score[0], score[1], score[2]), True,
                                                                 (255, 255, 255))
            score_label_rect = score_label.get_rect()
            score_label_rect.left = WIDTH / 2 * 0.3
            score_label_rect.centery = int(ratio * (2 + i))
            score_labels.append((score_label, score_label_rect))

        home_button = ControlBox(home_button_image, None, (WIDTH / 2 * 0.1, 50), (button_size, button_size))
        restart_button = ControlBox(restart_button_image, None, (WIDTH / 2 * 1.8, 50), (button_size, button_size))

        while running:
            screen.fill((0, 0, 0))
            screen.blit(menu_background, menu_background_rect)

            screen.blit(position_label, position_label_rect)

            screen.blit(home_button.image, home_button.rect)
            screen.blit(restart_button.image, restart_button.rect)

            for score_label_thingy in score_labels:
                screen.blit(score_label_thingy[0], score_label_thingy[1])

            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    running = False
                if event.type == MOUSEBUTTONUP and event.button == LEFT:
                    pos = pygame.mouse.get_pos()
                    if home_button.is_mouse_selection(pos):
                        running = False
                    if restart_button.is_mouse_selection(pos):
                        infile = open(settings_file, "r")
                        array = infile.readlines()
                        main.play_game(p1name, p2name, easy_selected, array[0], array[1], ship_location)
                        return
            pygame.display.update()
