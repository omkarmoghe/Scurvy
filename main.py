# Include everything here.
from Gameplay import *


def play_game(player1name, player2name):
    game = Gameplay(player1name, player2name, "Resources/Classic")
    game.run_game()