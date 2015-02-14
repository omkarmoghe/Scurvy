# Include everything here.
import Point
import Gameplay

global SCREEN_WIDTH, SCREEN_HEIGHT
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


def play_game():
    game = Gameplay.Gameplay(0, "Manav", "Evan", "Classic", Point(SCREEN_WIDTH, SCREEN_HEIGHT))
    game.run_game()

play_game()