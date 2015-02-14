import Ship


# This is the player ship object in the Game World. It has a nice initializer to create the Ship.
# It inherits from the Ship class.
class PlayerShip:

    def __init__(self, position):
        Ship.init(self, position, "PlayerShip0.png")
        self.health = 100

    # Overrides the Object's move so that rotating the ship is possible.
    def move(self, instruction_completed, move_to_y):
        max_y_speed = 10
        if instruction_completed:
            if move_to_y > self.rect.y:
                self.velocity.y += max_y_speed
            elif move_to_y < self.rect.y:
                self.velocity.y -= max_y_speed

        super.move(self)
        # TODO: Calculate rotation and choose correct image

    # Use this method to update the health. It returns true if the player ship is alive and
    # false if the player ship has no health left.
    def damage(self, damage_done):
        self.health -= damage_done
        if (self.health <= 0):
            return False
        return True