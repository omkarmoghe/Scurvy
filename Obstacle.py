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
        object_image = pygame.image.load(file_name)
        self.objectRect = object_image.get_rect()
        num_objects = self.screen_height / self.objectRect.height  # number of objects

        # add object to the obstacle_objects list
        point = Point(x_pos, self.objectRect.width / 2)
        for i in range(0, num_objects):
            point.x = random.randint(0, x_pos)
            obstacle = Object(point, file_name, velocity_ratio, Point(0, 0))
            self.obstacle_objects.append(obstacle)
            point.y += self.objectRect.height
            # TODO create gap

    def draw(self, screen):
        for obstacle in self.obstacle_objects:
            screen.blit(obstacle.image, obstacle.rect)

    # moves the objects in this obstacle
    def move(self, screen_width):
        for obstacle in self.obstacle_objects:
            obstacle.move()
            if obstacle.rect.right <= 0:
                # self.reset_position(screen_width)
                break

    def reset_position(self, screen_width):
        for obstacle in self.obstacle_objects:
            obstacle.rect.left = random.randint(0, screen_width)

    # returns the list of objects
    def get_obstacles(self):
        return self.obstacle_objects

    def set_velocity(self, velocity):
        for object in self.obstacle_objects:
            object.velocity.x = velocity.x
            object.velocity.y = velocity.y

    def check_collision(self, ship):
        for object in self.obstacle_objects:
            if pygame.sprite.collide_rect(object, ship):
                return self.damageGiven  # HEALTH LOST HERE
        return 0