import pygame
import PlayerShip
import Point

# This class creates the game play for the actual game.
class Gameplay():

    def __init__(self,difficulty, player1Name, player2Name, folder_name, screen_size):
        self.difficulty = difficulty
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.visualScreen = Point(screen_size.x, screen_size.y / 2)
        player_position = Point(self.visualScreen.x * 0.25, self.visualScreen.y / 2)
        self.playerShip = PlayerShip(player_position, folder_name)
        self.score = 0
        pygame.init()
        global WIDTH, HEIGHT, screen
        self.background = pygame.image.load("Resources/Background.png")
        self.backgroundRect = background.get_rect()
        WIDTH = screen_size.x
        HEIGHT = screen_size.y
        pygame.display.set_caption("Scurvy")
        screen = pygame.display.set_mode([screen_size.x, screen_size.y])

    def run_game(self):
        while True:
            self.update()

    def update(self):
        # TODO: Add stuff inside loop for game.
        screen.blit(background, backgroundRect)  # Always draw the background.