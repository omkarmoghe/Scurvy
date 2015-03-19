import random
from Object import *
from Point import *


velocity_ratio = 1.0  # speed of obstacle relative to other objects


class Obstacle():
    def __init__(self, x_pos, file_name, damage_given, screen_size):
        self.obstacle_objects = []  # list of obstacle objects
        self.damageGiven = damage_given  # damage given by this obstacle type

        # get height of object
        object_image = pygame.image.load(file_name)
        object_rect = object_image.get_rect()
        num_objects = screen_size.y / object_rect.height  # number of objects

        # add object to the obstacle_objects list
        point = Point(x_pos, object_rect.width / 2)
        for i in range(0, num_objects):
            point.x = random.randint(screen_size.x, screen_size.x * 2.0)
            point.y += object_rect.height
            obstacle = Object(point, file_name, velocity_ratio, Point(0, 0))
            self.obstacle_objects.append(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacle_objects:
            screen.blit(obstacle.image, obstacle.rect)

    # moves the objects in this obstacle
    def move(self, screen_width):
        for obstacle in self.obstacle_objects:
            obstacle.move()
            if obstacle.rect.right <= 0:
                reset_position(screen_width, obstacle)

    # returns the list of objects
    def get_obstacles(self):
        return self.obstacle_objects

    def set_velocity(self, velocity):
        for obj in self.obstacle_objects:
            obj.velocity.x = velocity.x
            obj.velocity.y = velocity.y

    def check_collision(self, ship):
        for obj in self.obstacle_objects:
            if pygame.sprite.collide_mask(obj, ship):
                return self.damageGiven  # HEALTH LOST HERE
        return 0


def reset_position(screen_width, this_obstacle):
        this_obstacle.rect.centerx = random.randint(screen_width, screen_width * 1.5)