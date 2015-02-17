import Object
import Point
import pygame
import random
from pygame import *

velocity_ratio = .5  # speed of obstacle relative to other objects


class Obstacle():
    def __init__(self, x_pos, file_name, damage_given):
        self.obstacle_objects = self.create_objects(file_name)
        self.gap = random.uniform(0, 800)
        self.screen_height = pygame.display.Info().current_h / 2
        self.damageGiven = damage_given
        self.x_pos = x_pos

=======


class Obstacle():
    def __init__(self, xPosition, file_name, damageGiven):
        self.obstacleObjects = []
        # self.yGapValue = random.uniform(0, 800)
>>>>>>> Gameplay-Branch
        # TODO: Add obstacles. Number of obstacles =  SCREEN_HEIGHT / SIZE_OF_OBJECT - 1 for all y locations
        rock = Object(Point(0, 0), file_name, velocity_ratio)
        num_objects = self.screen_height / 

    def move(self):
        for obstacle in self.obstacle_objects:
            obstacle.move(self)