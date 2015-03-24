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
        num_objects = (screen_size.y - 50) / object_rect.height  # number of objects
        num_objects -= 4
        # add object to the obstacle_objects list
        point = Point(x_pos, object_rect.width / 2)
        for i in range(0, num_objects):
            point.x = random.randint(screen_size.x, screen_size.x * 2.0)
            point.y += object_rect.height + 15
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
            point = pygame.sprite.collide_mask(obj, ship)
            if point:
                left = ship.rect
                right = obj.rect
                left_pos = max(left.left, right.left);
                right_pos = min(left.right, right.right);
                top = max(left.top, right.top);
                bottom = max(left.bottom, right.bottom);
                point_of_intersection = (left_pos + right_pos) / 2, (top + bottom) / 2
                # new_point = (point[0] + obj.rect.left, point[1] + obj.rect.top)
                return self.damageGiven, point_of_intersection  # HEALTH LOST HERE
        return 0, point


def reset_position(screen_width, this_obstacle):
        this_obstacle.rect.centerx = random.randint(screen_width, screen_width * 1.5)