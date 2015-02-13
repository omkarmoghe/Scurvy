import pygame
import Object


# This is a generic ship object in the Game World. It has a nice initializer to create the Ship.
# It inherits from the Object class.
class Ship(Object):

    def __init__(self, position, file_name):
        ship_ratio = 5
        Object.__init__(self, position, file_name, ship_ratio)

    def shoot(self, location):
        # bullet = Object("")
        # return bullet
        # TODO: Shoot at location