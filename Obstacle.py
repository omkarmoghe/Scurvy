import Object 

class Obstacle(Object):
    def __init__(self,damageGiven,position):
        Object.init()
        self.damageGiven  = damageGiven

    def drawObjects(self):
       