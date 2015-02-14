# Include everything here.
from Gameplay import *
from Point import *

global SCREEN_WIDTH, SCREEN_HEIGHT
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


def play_game():
    game = Gameplay(0, "Manav", "Evan", "Resources/Classic", Point(SCREEN_WIDTH, SCREEN_HEIGHT))
    game.run_game()

play_game()