from Object import *


# This is a generic ship object in the Game World. It has a nice initializer to create the Ship.
# It inherits from the Object class.
class Ship(Object):
    def __init__(self, position, file_name, image_ratio):
        ship_ratio = 5.0
        Object.__init__(self, position, file_name, ship_ratio, image_ratio)

    # This function determines how to move the ship based on the location of the player and
    # whether the instruction is completed
    '''def use_AI_to_move(self, location_of_player, instruction_completed):
        if (instruction_completed):
            assert False
            # TODO: IMPLEMENT ME TO MOVE AWAY FROM PLAYER
        else:
            assert False
            # TODO: IMPLEMENT ME TO MOVE TOWARD PLAYER '''