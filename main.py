# Include everything here.
from Gameplay import *


def play_game(player1name, player2name,difficulty_easy,sound_on,cheat_code):
    print "Player 1 name: " + player1name
    print "Player 2 name: " + player2name
    print "easy: "
    print difficulty_easy
    sound_on = sound_on[:len(sound_on)-1]
    print "sound on: " + sound_on
    print "cheat: " + cheat_code
    print "hi"
    game = Gameplay(player1name, player2name, "Resources/Classic",difficulty_easy,sound_on,cheat_code)
    game.run_game()