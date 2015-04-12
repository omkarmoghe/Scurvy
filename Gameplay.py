from PlayerShip import *
from HighScoreManager import *
from UserInputManager import *
from Obstacle import *
from Animations import *
from Globals import *


# This class creates the game play for the actual game.
class Gameplay():

    def __init__(self, player_1_name, player_2_name, folder_name, difficulty_easy, sound_on, cheat_code):
        pygame.display.set_caption(application_name)

        self.score_multiplier = 1

        self.player1Name = player_1_name
        self.player2Name = player_2_name
        self.visual_screen = (background_rect.width, background_rect.height)

        self.moving_background = Object((self.visual_screen[0] / 2, self.visual_screen[1] / 2),
                                        background_image, 0.5, (0, 0))
        self.moving_background_2 = Object((self.visual_screen[0] * 3 / 2, self.visual_screen[1] / 2),
                                          background_image, 0.5, (0, 0))
        player_position = (self.visual_screen[0] * 0.25, self.visual_screen[1] / 2)
        self.playerShip = PlayerShip(player_position, folder_name)

        self.difficulty_easy_select = difficulty_easy
        self.sound_on = True if sound_on == "On" else False
        self.explosion = 0

        self.score = 0
        self.user_manager = UserInputManager()
        self.collision_ended = True
        self.correct_sound = pygame.mixer.Sound(correct_press_sound)
        self.incorrect_sound = pygame.mixer.Sound(incorrect_press_sound)
        self.crash_sound = pygame.mixer.Sound(crash_sound)
        self.speed = standard_velocity
        self.rock_damage_multiplier = 1.0
        self.set_cheats(cheat_code)

        if difficulty_easy == 1:
            self.speed = standard_easy_velocity

        self.moving_background.velocity = self.moving_background_2.velocity = (standard_velocity, 0)
        self.obstacles = Obstacle(WIDTH, rock_image, rock_damage * self.rock_damage_multiplier,
                                  self.visual_screen)
        self.obstacles.set_velocity((self.speed, 0))
        self.background_music = pygame.mixer.music
        self.timer = pygame.time.get_ticks()

    def set_cheats(self, cheat_code):
        if cheat_code == "EDWARD":
            self.score_multiplier = score_cheat_multiplier
        elif cheat_code == "EVAN":
            self.rock_damage_multiplier = rock_damage_cheat_multiplier
        elif cheat_code == "MANAV":
            self.score = initial_cheat_score
        elif cheat_code == "OMKAR":
            self.playerShip.fuel = initial_cheat_fuel
        elif cheat_code == "CHESNEY":
            self.score_multiplier = score_cheat_multiplier
            self.rock_damage_multiplier = rock_damage_cheat_multiplier
            self.score = initial_cheat_score
            self.playerShip.fuel = initial_cheat_fuel

    def run_game(self):
        running = True
        self.background_music = pygame.mixer.music
        self.background_music.load(background_sound)
        if self.sound_on:
            self.background_music.play(-1, 0.0)
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
                        self.playerShip.damage(bad_instruction_damage)
                    elif score_value:
                        self.instructions_completed(score_value)
                        if self.speed > max_velocity:
                            self.speed += acceleration
                        self.obstacles.set_velocity((self.speed, 0))

    def game_over(self):
        self.background_music.stop()
        high_score_manager = HighScoreManager(high_score_file)
        high_score_manager.add_high_score((self.player1Name, self.player2Name, self.score))
        high_score_manager.draw(self.player1Name, self.player2Name, self.difficulty_easy_select,
                                self.playerShip.folder_name)

    def instructions_completed(self, add_score):
        if self.sound_on:
            self.correct_sound.play()
        self.playerShip.fuel += fuel_amount
        self.score += add_score * self.score_multiplier
        self.user_manager.instructions = []
        self.user_manager.populate_random_panel_instructions(4, self.score)
        self.user_manager.set_player_instructions()

    def update(self):
        screen.fill(BLACK)
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
        pygame.draw.line(screen, WHITE, (WIDTH / 2, self.visual_screen[1] + 1), (WIDTH / 2, HEIGHT), 5)
        self.draw_score_and_health()
        if self.playerShip.fuel > 0:
            keys = pygame.key.get_pressed()
            self.playerShip.input(keys)
        self.playerShip.move(self.speed, self.visual_screen[1])
        damage_and_point = self.obstacles.check_collision(self.playerShip)
        if damage_and_point[0]:
            if self.collision_ended:
                point = damage_and_point[1][0] - size_of_explosion + 28, damage_and_point[1][1] - size_of_explosion
                # 28 is the only hard coded variable we have x_x, but we have no choice.
                self.explosion = Animations((size_of_explosion, size_of_explosion), explosion_image,
                                            point)
                self.playerShip.damage(damage_and_point[0])
                if self.sound_on:
                    self.crash_sound.play()
                self.collision_ended = False
                if self.playerShip.fuel >= collision_fuel_punishment:
                    self.playerShip.fuel -= collision_fuel_punishment
                else:
                    self.playerShip.fuel = 0

            if self.explosion != 0:
                self.explosion.update_animation(self.timer)
        else:
            self.collision_ended = True
        pygame.display.update()

    def draw_instruction_panel(self):
        for display_instruction in self.user_manager.current_instructions:
            display_instruction.draw(self.visual_screen[1])

        offset2 = 80 + self.visual_screen[1]
        control_label = pygame.font.Font(font_file, 20).render('Controls', True, YELLOW)
        control_label2 = pygame.font.Font(font_file, 20).render('Controls', True, YELLOW)
        control_label_rect = control_label.get_rect()
        control_label_rect2 = control_label2.get_rect()
        control_label_rect.centery = offset2
        control_label_rect2.centery = offset2
        control_label_rect.centerx = WIDTH * 1 / 4
        control_label_rect2.centerx = WIDTH * 3 / 4
        screen.blit(control_label, control_label_rect)
        screen.blit(control_label2, control_label_rect2)

        offset = 112 + self.visual_screen[1]

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
                                                                True, GREEN)
        player_1_label_rect = player_1_label.get_rect()
        player_1_label_rect.centerx = WIDTH / 4
        player_1_label_rect.top = self.visual_screen[1] + 5
        player_2_label = pygame.font.Font(font_file, 18).render('{0}'.format(self.player2Name),
                                                                True, GREEN)
        player_2_label_rect = player_2_label.get_rect()
        player_2_label_rect.centerx = 3 * WIDTH / 4
        player_2_label_rect.top = self.visual_screen[1] + 5
        screen.blit(player_1_label, player_1_label_rect)
        screen.blit(player_2_label, player_2_label_rect)

        score_label = pygame.font.Font(font_file, 15).render('{0}'.format("SCORE: " + str(self.score)) + "             "
                                                                                                         "FUEL: "
                                                             + str(self.playerShip.fuel), True, WHITE)
        score_label_rect = score_label.get_rect()
        score_label_rect.centerx = WIDTH / 4
        score_label_rect.top = HEIGHT - 20
        screen.blit(score_label, score_label_rect)

        red_bar = pygame.image.load(healthbar_image)
        green_bar = pygame.image.load(health_image)
        health_value = self.playerShip.health

        screen.blit(red_bar, (WIDTH * 5 / 8, HEIGHT - 20))
        for thisHealth in range(int(health_value)):
            screen.blit(green_bar, (thisHealth + WIDTH * 5 / 8, HEIGHT - 17))
