from Object import *


# This is a generic ship object in the Game World. It has a nice initializer to create the Ship.
# It inherits from the Object class.
class Ship(Object):
    def __init__(self, position, file_name, image_ratio):
        ship_ratio = 5.0
        Object.__init__(self, position, file_name, ship_ratio, image_ratio)
