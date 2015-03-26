import os.path
from pygame import *
import pygame
import main

font_file = "Resources/font.otf"

# HIGH SCORES FORMAT IS AS FOLLOWS:
#     Player1:Player2:score
# ex. Bart:Lisa:400
class HighScoreManager():

    def __init__(self, filename):
        self.filename = filename
        self.highscores = self.load_high_scores()
        self.sort_high_scores()

    def load_high_scores(self):
        if not os.path.isfile(self.filename):
            f_out = open(self.filename, 'w')
            f_out.close()

        high_scores = []

        f_in = open(self.filename, 'r')
        for line in f_in:
            set = line.split(':')  # split the line at the colon
            high_scores.append((set[0], set[1], int(set[2])))  # first half is name, second half is score

        f_in.close()

        return high_scores

    def save_high_scores(self):
        self.sort_high_scores()

        f_out = open(self.filename, 'w')

        for pair in self.highscores:
            f_out.write(pair[0] + ':' + pair[1] + ':' + str(pair[2]) + '\n')

        f_out.close()

    def sort_high_scores(self):
        self.highscores.sort(key=lambda tup: tup[2])
        self.highscores.reverse()

    # set is a tuple (Player1, Player2, score)
    def add_high_score(self, set):
        if len(self.highscores) < 10:
            self.sort_high_scores()
            self.highscores.append(set)
            self.sort_high_scores()
            self.save_high_scores()
        elif len(self.highscores) == 10:
            self.highscores.append(set)
            self.sort_high_scores()
            del self.highscores[-1]
            self.save_high_scores()
        else:
            assert False  # should never be the case

    def draw(self, screen, p1name, p2name, easy_selected):
        background = pygame.image.load("Resources/MenuBackground.png")
        backgroundRect = background.get_rect()
        running = True
        position_label = pygame.font.Font(font_file, 25).render('High Scores Table', True, (255, 255, 255))
        position_label_rect = position_label.get_rect()
        center_x = screen.get_width() / 2
        position_label_rect.centerx = center_x
        ratio = screen.get_height() / 12
        position_label_rect.centery = int(ratio)
        score_labels = []
        for (i, score) in enumerate(self.highscores):
            score_label = pygame.font.Font(font_file, 20).render('{0:12s} {1:12s} scored {2:10d} points.'.format
                                                                 (score[0], score[1], score[2]), True,
                                                                 (255, 255, 255))
            score_label_rect = score_label.get_rect()
            score_label_rect.left = center_x * 0.3
            score_label_rect.centery = int(ratio * (2 + i))
            score_labels.append((score_label, score_label_rect))

        home_button = pygame.image.load("Resources/Home.png")
        home_button = pygame.transform.scale(home_button, (60, 60))
        home_button_rect = home_button.get_rect()
        home_button_rect.centery = 50
        home_button_rect.centerx = center_x * 0.1
        restart_button = pygame.image.load("Resources/Restart.png")
        restart_button = pygame.transform.scale(restart_button, (60, 60))
        restart_button_rect = restart_button.get_rect()
        restart_button_rect.centery = 50
        restart_button_rect.centerx = center_x * 1.8
        while running:
            screen.fill((0, 0, 0))
            screen.blit(background, backgroundRect)
            screen.blit(position_label, position_label_rect)
            screen.blit(home_button, home_button_rect)
            screen.blit(restart_button, restart_button_rect)
            for score_label_thingy in score_labels:
                screen.blit(score_label_thingy[0], score_label_thingy[1])
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    running = False
                if event.type == MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if home_button_rect.collidepoint(pos):
                        running = False
                    if restart_button_rect.collidepoint(pos):
                        infile = open("sound_and_cheat.txt", "r")
                        array = infile.readlines()
                        main.play_game(p1name, p2name, easy_selected, array[0], array[1])
                        return
            pygame.display.update()

# FOR TESTING ONLY
# hsm = HighScoreManager("highscores.txt")
# pygame.init()
# background_image = "Resources/Background.png"
# background = pygame.image.load(background_image)
# backgroundRect = background.get_rect()
# WIDTH = backgroundRect.width
# HEIGHT = 3 * backgroundRect.height / 2
# screen = pygame.display.set_mode([WIDTH, HEIGHT])
# hsm.draw(screen)
