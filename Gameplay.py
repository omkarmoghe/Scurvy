import pygame
from pygame.locals import *
from PlayerShip import *
from Point import *
from UserInputManager import *


# This class creates the game play for the actual game.
class Gameplay():

    def __init__(self, difficulty, player_1_name, player_2_name, folder_name):
        pygame.init()
        global WIDTH, HEIGHT, screen
        pygame.display.set_caption("Scurvy")
        self.background = pygame.image.load("Resources/Background.png")
        self.backgroundRect = self.background.get_rect()
        WIDTH = self.backgroundRect.width
        HEIGHT = 3 * self.backgroundRect.height / 2
        print HEIGHT
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.difficulty = difficulty
        self.player1Name = player_1_name
        self.player2Name = player_2_name
        self.visual_screen = Point(self.backgroundRect.width, self.backgroundRect.height)
        player_position = Point(self.visual_screen.x * 0.25, self.visual_screen.y / 2)
        self.playerShip = PlayerShip(player_position, folder_name)
        self.score = 0
        self.user_manager = UserInputManager

    def run_game(self):
        running = True
        while running:
            self.update()
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    running = False
                if event.type == KEYDOWN:
                    self.user_manager.check_inputs(event.key)

    def update(self):
        screen.blit(self.background, self.backgroundRect)  # Always draw the background.
        screen.blit(self.playerShip.image, self.playerShip.rect)
        # TODO: Add stuff inside loop for game.
        pygame.display.update()

    def draw_instruction(self, playerNumber, stringForInstruction):
        if playerNumber == 0:
            assert False
            # TODO: Something
        elif playerNumber == 1:
            assert False
            # TODO: Something else

    def draw_score_and_health(self):
        assert False
        # TODO: Draw score and health here.