import random

from Object import *
from Point import *


velocity_ratio = .5  # speed of obstacle relative to other objects


class Obstacle():
    def __init__(self, x_pos, file_name, damage_given, screen_height):
        self.obstacle_objects = []  # list of obstacle objects
        self.gap = random.uniform(0, screen_height)  # location of gap (not used as of alpha release)
        self.screen_height = screen_height  # height of graphics screen
        self.damageGiven = damage_given  # damage given by this obstacle type
        self.x_pos = x_pos  # x position of obstacle

        # get height of object
        obj = Object(Point(0, 0), file_name, velocity_ratio)
        self.object_height = obj.rect.height

        num_objects = self.screen_height / self.object_height - 2  # number of objects

        # add object to the obstacle_objects list
        point = Point(x_pos, 0)
        for i in range(0, num_objects):
            obst = Object(point, file_name, velocity_ratio)
            self.obstacle_objects.append(obst)
            point.y += self.object_height
            # TODO create gap

    # moves the objects in this obstacle
    def move(self):
        for obstacle in self.obstacle_objects:
            obstacle.move(self)

    # returns the list of objects
    def get_obstacles(self):
        return self.obstacle_objects