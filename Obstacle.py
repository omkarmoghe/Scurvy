import random
import pygame
from Object import *
from Point import *


velocity_ratio = 1.0  # speed of obstacle relative to other objects


class Obstacle():
    def __init__(self, x_pos, file_name, damage_given, screen_height):
        self.obstacle_objects = []  # list of obstacle objects
        self.gap = random.uniform(0, screen_height)  # location of gap (not used as of alpha release)
        self.screen_height = screen_height  # height of graphics screen
        self.damageGiven = damage_given  # damage given by this obstacle type

        # get height of object
        objectImage = pygame.image.load(file_name)
        self.objectRect = objectImage.get_rect()
        self.x_pos = x_pos + self.objectRect.width / 2 # x position of obstacle
        num_objects = self.screen_height / self.objectRect.height  # number of objects

        # add object to the obstacle_objects list
        point = Point(x_pos, self.objectRect.width / 2)
        for i in range(0, num_objects):
            obst = Object(point, file_name, velocity_ratio, Point(0,0))
            self.obstacle_objects.append(obst)
            point.y += self.objectRect.height
            # TODO create gap

    def draw(self, screen):
        for object in self.obstacle_objects:
            screen.blit(object.image, object.rect)

    # moves the objects in this obstacle
    def move(self, screen_width):
        for obstacle in self.obstacle_objects:
            obstacle.move()
            if obstacle.rect.right <= 0:
                obstacle.rect.left = screen_width

    # returns the list of objects
    def get_obstacles(self):
        return self.obstacle_objects

    def set_velocity(self, velocity):
        for obstacle in self.obstacle_objects:
            obstacle.velocity.x = velocity.x
            obstacle.velocity.y = velocity.y

    # checks collision against rocks
    def check_collision(self, ship):
        for object in self.obstacle_objects:
            if pygame.sprite.collide_rect(object, ship):
                return True  # HEALTH LOST HERE
        return False