import pygame
from PlayerShip import *
from Point import *


# This class creates the game play for the actual game.
class Gameplay():

    def __init__(self, difficulty, player_1_name, player_2_name, folder_name, screen_size):
        global WIDTH, HEIGHT, screen
        pygame.display.set_caption("Scurvy")
        self.background = pygame.image.load("Resources/Background.png")
        self.backgroundRect = self.background.get_rect()
        WIDTH = screen_size.x
        HEIGHT = screen_size.y
        screen = pygame.display.set_mode([screen_size.x, screen_size.y])

        self.difficulty = difficulty
        self.player1Name = player_1_name
        self.player2Name = player_2_name
        self.visual_screen = Point(screen_size.x, screen_size.y / 2)
        player_position = Point(self.visual_screen.x * 0.25, self.visual_screen.y / 2)
        self.playerShip = PlayerShip(player_position, folder_name)
        self.score = 0
        pygame.init()

    def run_game(self):
        while True:
            self.update()

    def update(self):
        # TODO: Add stuff inside loop for game.
        screen.blit(self.background, self.backgroundRect)  # Always draw the background.