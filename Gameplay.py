import pygame
from pygame.locals import *
from PlayerShip import *
from UserInputManager import *
from Obstacle import *
from Point import *

standard_velocity = -2
background_image = "Resources/Background.png"
rock_damage = 40
global font_file
font_file = "Resources/font.otf"


# This class creates the game play for the actual game.
class Gameplay():

    def __init__(self, difficulty, player_1_name, player_2_name, folder_name):
        pygame.init()
        global WIDTH, HEIGHT, screen
        pygame.display.set_caption("Scurvy")
        self.background = pygame.image.load(background_image)
        self.backgroundRect = self.background.get_rect()
        WIDTH = self.backgroundRect.width
        HEIGHT = 3 * self.backgroundRect.height / 2
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.difficulty = difficulty
        self.player1Name = player_1_name
        self.player2Name = player_2_name
        self.visual_screen = Point(self.backgroundRect.width, self.backgroundRect.height)
        self.moving_background = Object(Point(self.visual_screen.x / 2, self.visual_screen.y / 2),
                                        background_image, 0.5, Point(0, 0))
        self.moving_background_2 = Object(Point(self.visual_screen.x * 3 / 2, self.visual_screen.y / 2),
                                            background_image, 0.5, Point(0, 0))
        player_position = Point(self.visual_screen.x * 0.25, self.visual_screen.y / 2)
        self.playerShip = PlayerShip(player_position, folder_name)
        self.obstacles = Obstacle(WIDTH, "Resources/rock_single.png", rock_damage, self.visual_screen.y)

        self.obstacles.set_velocity(Point(standard_velocity, 0))
        self.moving_background.velocity.x = self.moving_background_2.velocity.x = standard_velocity
        self.score = 0
        self.user_manager = UserInputManager()
        self.collision_ended = True
        self.correct_sound = pygame.mixer.Sound('Resources/correct_press.wav')
        self.incorrect_sound = pygame.mixer.Sound('Resources/incorrect_press.wav')
        self.crash_sound = pygame.mixer.Sound('Resources/crash.wav')


    def run_game(self):
        running = True
        background_music = pygame.mixer.music
        background_music.load('Resources/background_music1.wav')
        background_music.play(-1, 0.0)

        # THESE ARE HARD CODED COMPLEXITIES THAT WE NEED TO CHANGE IN BETA
        self.user_manager.populate_random_panel_instructions(4, 1)
        self.user_manager.set_player_instructions()
        while running:
            self.update()
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    running = False
                if event.type == KEYDOWN and self.obstacles.obstacle_objects[0].rect.left > self.playerShip.rect.right:
                    score_value = self.user_manager.check_inputs(event.key)
                    if score_value == -1:
                        self.incorrect_sound.play()
                        self.playerShip.damage(10)
                    elif score_value:
                        self.instructions_completed(score_value)


    def instructions_completed(self, add_score):
        self.correct_sound.play()
        self.obstacles.reset_position(WIDTH)
        self.score += add_score
        self.user_manager.instructions = []
        self.user_manager.populate_random_panel_instructions(4, 1)
        self.user_manager.set_player_instructions()

    def update(self):

        screen.fill((0, 0, 0))
        screen.blit(self.moving_background.image, self.moving_background.rect)
        screen.blit(self.moving_background_2.image, self.moving_background_2.rect)
        self.obstacles.draw(screen)
        self.draw_instruction_panel()
        screen.blit(self.playerShip.image, self.playerShip.rect)
        if self.moving_background.rect.right <= 0:
            self.moving_background.rect.left = WIDTH
        if self.moving_background_2.rect.right <= 0:
            self.moving_background_2.rect.left = WIDTH
        self.obstacles.move(WIDTH)
        self.moving_background.move()
        self.moving_background_2.move()
        pygame.draw.line(screen, (255, 255, 255, 1.0), (WIDTH / 2, self.visual_screen.y + 1), (WIDTH / 2, HEIGHT), 5)
        self.draw_score_and_health()
        damage = self.obstacles.check_collision(self.playerShip)
        if damage:
            if self.collision_ended:
                self.playerShip.damage(damage)
                self.crash_sound.play()
                self.collision_ended = False
        else:
            self.collision_ended = True
        # TODO: Add stuff inside loop for game.
        pygame.display.update()

    def draw_instruction_panel(self):
        for display_instruction in self.user_manager.current_instructions:
            display_instruction.draw(screen, self.visual_screen)

        offset = 80 + self.visual_screen.y

        for (i, instruction) in enumerate(self.user_manager.instructions):
            instruction_label = pygame.font.Font(font_file, 15).render('{0}'.format(instruction.get_message()),
                                                                                        True, (255, 255, 255))
            instruction_label_rect = instruction_label.get_rect()
            instruction_label_rect.centery = offset + i * 30
            if i >= len(self.user_manager.instructions) / 2:
                instruction_label_rect.centery = offset + (i - (len(self.user_manager.instructions) / 2)) * 30
            if instruction.player_number == 0:
                instruction_label_rect.centerx = WIDTH * 1 / 4
            elif instruction.player_number == 1:
                instruction_label_rect.centerx = WIDTH * 3 / 4
            else:
                assert False
            screen.blit(instruction_label, instruction_label_rect)


    def draw_score_and_health(self):
        player1Label = pygame.font.Font(font_file, 15).render('{0}'.format(self.player1Name),
                                                                                        True, (255, 255, 255))
        player1LabelRect = player1Label.get_rect()
        player1LabelRect.centerx = WIDTH / 4
        player1LabelRect.top = self.visual_screen.y + 5
        player2Label = pygame.font.Font(font_file, 15).render('{0}'.format(self.player2Name),
                                                                                        True, (255, 255, 255))
        player2LabelRect = player2Label.get_rect()
        player2LabelRect.centerx = 3 * WIDTH / 4
        player2LabelRect.top = self.visual_screen.y + 5
        screen.blit(player1Label, player1LabelRect)
        screen.blit(player2Label, player2LabelRect)

        scoreLabel = pygame.font.Font(font_file, 15).render('{0}'.format("SCORE: " + str(self.score)), True, (255, 255,
                                                                                                              255))
        scoreLabelRect = scoreLabel.get_rect()
        scoreLabelRect.centerx = WIDTH / 4
        scoreLabelRect.top = HEIGHT - 20
        screen.blit(scoreLabel, scoreLabelRect)
        
        red_bar = pygame.image.load("Resources/healthbar.png")
        green_bar = pygame.image.load("Resources/health.png")
        health_value = self.playerShip.health
        
        screen.blit(red_bar, (WIDTH * 5 / 8, HEIGHT - 20))
        for thisHealth in range(health_value):
            screen.blit(green_bar, (thisHealth + WIDTH * 5 / 8, HEIGHT - 17))