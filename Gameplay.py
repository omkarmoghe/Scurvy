from PlayerShip import *
from HighScoreManager import *
from UserInputManager import *
from Obstacle import *
from Point import *
import sys
from Animations import *

background_image = "Resources/Background.png"  # Adjust this to change the background image.
standard_velocity = -1.0  # Adjust this to change the starting velocity. WARNING: Must be negative for rightwards motion
max_velocity = -5.1  # Adjust to change the upper bound of the velocity. WARNING: Must be less than standard_velocity
acceleration = -0.1  # Adjust this to change how much the velocity changes per instruction got correct.
rock_damage = 40  # Adjust this to change the amount of damage a Rock does.
font_file = "Resources/font.otf"
fuel_amount = 100  # Adjust this to change how much time to give to the player after correctly performing an instruction
# We are using -1 here so that we can test moving the boat. TODO: Change this value to 50 or there about.
collision_fuel_punishment = 20
size_of_explosion = 128  # Adjust this to change the size of the explosion animation thingy.
back_overlap = 5  # Adjust this to change how much the two backgrounds overlap so that there are no creases.
high_score_file = "highscores.txt"

# This class creates the game play for the actual game.
class Gameplay():

    def __init__(self, player_1_name, player_2_name, folder_name, difficulty_easy, sound_on, cheat_code):
        global standard_velocity

        pygame.init()
        global WIDTH, HEIGHT, screen
        pygame.display.set_caption("Scurvy")


        self.score_multiplier = 1
        self.background = pygame.image.load(background_image)
        self.backgroundRect = self.background.get_rect()
        WIDTH = self.backgroundRect.width
        HEIGHT = 3 * self.backgroundRect.height / 2
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.player1Name = player_1_name
        self.player2Name = player_2_name
        self.visual_screen = Point(self.backgroundRect.width, self.backgroundRect.height)
        self.moving_background = Object(Point(self.visual_screen.x / 2, self.visual_screen.y / 2),
                                        background_image, 0.5, Point(0, 0))
        self.moving_background_2 = Object(Point(self.visual_screen.x * 3 / 2, self.visual_screen.y / 2),
                                          background_image, 0.5, Point(0, 0))
        player_position = Point(self.visual_screen.x * 0.25, self.visual_screen.y / 2)
        self.playerShip = PlayerShip(player_position, folder_name)
        # self.give_control = 0  # Useful for moving the ship around
        self.difficulty_easy_select = difficulty_easy
        self.sound_on = True if sound_on == "On" else False
        self.explosion = 0
        self.moving_background.velocity.x = self.moving_background_2.velocity.x = standard_velocity
        self.score = 0
        self.user_manager = UserInputManager()
        self.collision_ended = True
        self.correct_sound = pygame.mixer.Sound('Resources/correct_press.wav')
        self.incorrect_sound = pygame.mixer.Sound('Resources/incorrect_press.wav')
        self.crash_sound = pygame.mixer.Sound('Resources/crash.wav')
        self.speed = standard_velocity

        self.set_cheats(cheat_code)
        if difficulty_easy == 0:
            standard_velocity = -2.5

        self.obstacles = Obstacle(WIDTH, "Resources/rock_single.png", rock_damage, self.visual_screen)
        self.obstacles.set_velocity(Point(standard_velocity, 0))

    def set_cheats(self, cheat_code):
        global rock_damage

        if cheat_code == "EDWARD":
            self.score_multiplier = 1.5
        elif cheat_code == "EVAN":
            rock_damage = 20
        elif cheat_code == "MANAV":
            self.score = 200
        elif cheat_code == "OMKAR":
            self.playerShip.fuel = 200
        elif cheat_code == "CHESNEY":
            self.score_multiplier = 1.5
            self.playerShip.fuel = 200
            self.score = 200
            rock_damage = 20

    def run_game(self):
        running = True
        background_music = pygame.mixer.music
        background_music.load('Resources/pirate_music.wav')
        if self.sound_on:
            background_music.play(-1, 0.0)
        self.user_manager.populate_random_panel_instructions(4, 0)  # Zero is default mean
        self.user_manager.set_player_instructions()
        while running:
            self.timer = pygame.time.get_ticks()
            self.update()
            if self.playerShip.health <= 0:
                running = False
                self.game_over()
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    self.playerShip.health = 0
                if event.type == KEYDOWN:
                    score_value = self.user_manager.check_inputs(event.key)
                    if score_value == -1:
                        if self.sound_on:
                            self.incorrect_sound.play()
                        self.playerShip.damage(10)
                    elif score_value:
                        self.instructions_completed(score_value)
                        if self.speed > max_velocity:
                            self.speed += acceleration
                        self.obstacles.set_velocity(Point(self.speed, 0))

    def game_over(self):
        highscore_manager = HighScoreManager(high_score_file)
        highscore_manager.add_high_score((self.player1Name, self.player2Name, self.score))
        highscore_manager.draw(screen, self.player1Name, self.player2Name, self.difficulty_easy_select)

    def instructions_completed(self, add_score):
        if self.sound_on:
            self.correct_sound.play()
        self.playerShip.fuel += fuel_amount
        self.score += add_score * self.score_multiplier
        self.user_manager.instructions = []
        self.user_manager.populate_random_panel_instructions(4, self.score)
        self.user_manager.set_player_instructions()

    def update(self):
        screen.fill((0, 0, 0))
        screen.blit(self.moving_background.image, self.moving_background.rect)
        screen.blit(self.moving_background_2.image, self.moving_background_2.rect)
        self.obstacles.draw(screen)
        self.draw_instruction_panel()
        screen.blit(self.playerShip.image, self.playerShip.rect)
        if self.moving_background.rect.right <= 0:
            self.moving_background.rect.left = self.moving_background_2.rect.right - back_overlap
        if self.moving_background_2.rect.right <= 0:
            self.moving_background_2.rect.left = self.moving_background.rect.right - back_overlap
        self.obstacles.move(WIDTH)
        self.moving_background_2.move()
        self.moving_background.move()
        pygame.draw.line(screen, (255, 255, 255, 1.0), (WIDTH / 2, self.visual_screen.y + 1), (WIDTH / 2, HEIGHT), 5)
        self.draw_score_and_health()
        if self.playerShip.fuel > 0:
            keys = pygame.key.get_pressed()
            self.playerShip.input(keys)
        self.playerShip.move(self.speed, self.visual_screen.y)
        damage_and_point = self.obstacles.check_collision(self.playerShip)
        if damage_and_point[0]:
            if self.collision_ended:
                point = damage_and_point[1][0] - size_of_explosion + 28, damage_and_point[1][1] - size_of_explosion
                # 28 is the only hard coded variable we have x_x but we have no choice.
                self.explosion = Animations(size_of_explosion, size_of_explosion, "Resources/explosion.png",
                                            point, screen)
                self.playerShip.damage(damage_and_point[0])
                if self.sound_on:
                    self.crash_sound.play()
                self.collision_ended = False
                if self.playerShip.fuel >= 20:
                    self.playerShip.fuel -= collision_fuel_punishment
                else:
                    self.playerShip.fuel = 0

                # self.give_control = 0
            if self.explosion != 0:
                self.explosion.updateAnimation(self.timer)
        else:
            self.collision_ended = True
        # TODO: Add stuff inside loop for game.
        pygame.display.update()

    def draw_instruction_panel(self):
        for display_instruction in self.user_manager.current_instructions:
            display_instruction.draw(screen, self.visual_screen)

        offset2 = 80 + self.visual_screen.y
        control_label = pygame.font.Font(font_file, 20).render('Controls', True, (255, 255, 0))
        control_label2 = pygame.font.Font(font_file, 20).render('Controls', True, (255, 255, 0))
        control_label_rect = control_label.get_rect()
        control_label_rect2 = control_label2.get_rect()
        control_label_rect.centery = offset2
        control_label_rect2.centery = offset2
        control_label_rect.centerx = WIDTH * 1 / 4
        control_label_rect2.centerx = WIDTH * 3 / 4
        screen.blit(control_label, control_label_rect)
        screen.blit(control_label2, control_label_rect2)

        offset = 112 + self.visual_screen.y

        for (i, instruction) in enumerate(self.user_manager.instructions):
            instruction_label = pygame.font.Font(font_file, 15).render('{0}'.format(instruction.get_message()),
                                                                       True, (102, 178, 255))
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
        player_1_label = pygame.font.Font(font_file, 18).render('{0}'.format(self.player1Name),
                                                                True, (0, 255, 0))
        player_1_label_rect = player_1_label.get_rect()
        player_1_label_rect.centerx = WIDTH / 4
        player_1_label_rect.top = self.visual_screen.y + 5
        player_2_label = pygame.font.Font(font_file, 18).render('{0}'.format(self.player2Name),
                                                                True, (0, 255, 0))
        player_2_label_rect = player_2_label.get_rect()
        player_2_label_rect.centerx = 3 * WIDTH / 4
        player_2_label_rect.top = self.visual_screen.y + 5
        screen.blit(player_1_label, player_1_label_rect)
        screen.blit(player_2_label, player_2_label_rect)

        score_label = pygame.font.Font(font_file, 15).render('{0}'.format("SCORE: " + str(self.score)) + "             "
                                                                                                         "FUEL: "
                                                             + str(self.playerShip.fuel), True, (255, 255, 255))
        score_label_rect = score_label.get_rect()
        score_label_rect.centerx = WIDTH / 4
        score_label_rect.top = HEIGHT - 20
        screen.blit(score_label, score_label_rect)

        red_bar = pygame.image.load("Resources/healthbar.png")
        green_bar = pygame.image.load("Resources/health.png")
        health_value = self.playerShip.health

        screen.blit(red_bar, (WIDTH * 5 / 8, HEIGHT - 20))
        for thisHealth in range(health_value):
            screen.blit(green_bar, (thisHealth + WIDTH * 5 / 8, HEIGHT - 17))
