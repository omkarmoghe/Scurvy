import pygame
from pygame.locals import *
from PlayerShip import *
from UserInputManager import *
from Rock import *
from Point import *

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
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.difficulty = difficulty
        self.player1Name = player_1_name
        self.player2Name = player_2_name
        self.visual_screen = Point(self.backgroundRect.width, self.backgroundRect.height)
        self.moving_background = Object(Point(self.visual_screen.x / 2, self.visual_screen.y / 2),
                                        "Resources/Background.png", 0.5, Point(0, 0))
        self.moving_background_2 = Object(Point(self.visual_screen.x * 3 / 2, self.visual_screen.y / 2),
                                            "Resources/Background2.png", 0.5, Point(0, 0))
        player_position = Point(self.visual_screen.x * 0.25, self.visual_screen.y / 2)
        self.playerShip = PlayerShip(player_position, folder_name)
        self.rock = Rock(Point(WIDTH, 0))
        self.rock.velocity.x = self.moving_background.velocity.x = self.moving_background_2.velocity.x = -2
        self.score = 0
        self.user_manager = UserInputManager()

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
        screen.blit(self.moving_background.image, self.moving_background.rect)
        screen.blit(self.moving_background_2.image, self.moving_background_2.rect)
        screen.blit(self.rock.image, self.rock.rect)
        screen.blit(self.playerShip.image, self.playerShip.rect)
        if self.moving_background.rect.right <= 0:
            self.moving_background.rect.left = WIDTH
        if self.moving_background_2.rect.right <= 0:
            self.moving_background_2.rect.left = WIDTH
        self.rock.move(WIDTH)
        self.moving_background.move()
        self.moving_background_2.move()
        pygame.draw.line(screen, (255, 255, 255, 1.0), (WIDTH / 2, self.visual_screen.y + 1), (WIDTH / 2, HEIGHT), 5)
        self.draw_score_and_health()
        if self.rock.check_collision(self.playerShip):
            print "Collision Detected YAY"
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
        player1Label = pygame.font.Font('Resources/SourceCodePro-Light.otf', 15).render('{0}'.format(self.player1Name), True, (255, 255,
                                                                                                              255))
        player1LabelRect = player1Label.get_rect()
        player1LabelRect.centerx = WIDTH / 4
        player1LabelRect.top = self.visual_screen.y + 5
        player2Label = pygame.font.Font('Resources/SourceCodePro-Light.otf', 15).render('{0}'.format(self.player2Name), True, (255, 255,
                                                                                                              255))
        player2LabelRect = player2Label.get_rect()
        player2LabelRect.centerx = 3 * WIDTH / 4
        player2LabelRect.top = self.visual_screen.y + 5
        screen.blit(player1Label, player1LabelRect)
        screen.blit(player2Label, player2LabelRect)

        # TODO: Draw score and health here.