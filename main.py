# Include everything here.
from Gameplay import *
from Point import *



def play_game():
    game = Gameplay("Chesney", "Chesney 2.O", "Resources/Classic")
    game.run_game()

play_game()