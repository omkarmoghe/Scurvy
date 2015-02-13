import Ship


# This is the player ship object in the Game World. It has a nice initializer to create the Ship.
# It inherits from the Ship class.
class PlayerShip:

    def __init__(self, position):
        Ship.init(self, position, "PlayerShip0.png")
        self.health = 100

    def move(self):
        super.move(self)
        # TODO: Calculate rotation and choose correct image
    
    def damage(self, damage_done):
        self.health -= damage_done