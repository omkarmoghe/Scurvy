import pygame

class Gameplay():
    def __init__(self,difficulty,player1Name,player2Name,flagColor):
        self.difficulty = difficulty
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.flagColor = flagColor
        self.score = 0
        if difficulty == 'easy':
            #self.timer = 10
        else:
            #self.timer = 5
        
        
        
    def update(self):
        

        