

class Obstacle():
    def __init__(self, xPosition, file_name, damageGiven):
        self.obstacleObjects = []
        # self.yGapValue = random.uniform(0, 800)
        # TODO: Add obstacles. Number of obstacles =  SCREEN_HEIGHT / SIZE_OF_OBJECT - 1 for all y locations
        # except for at y gap value.
        self.damageGiven = damageGiven

    def move(self):
        for obstacle in self.obstacleObjects:
            obstacle.move(self)