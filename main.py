# Include everything here.
from Globals import *
import Gameplay
import sys
from MainMenu import *


def play_game(player1name, player2name, difficulty_easy, sound_on, cheat_code):
    sound_on = sound_on[:len(sound_on)-1]
    # print "Player 1 name: " + player1name
    # print "Player 2 name: " + player2name
    # print "Difficulty: "
    # print difficulty_easy
    # print "Sound on: " + sound_on
    # print "Cheat: " + cheat_code
    # TODO: Allow ship customization
    game = Gameplay.Gameplay(player1name, player2name, classic_ship_location, difficulty_easy, sound_on, cheat_code)
    game.run_game()

if __name__ == "__main__":
    # Creating the screen
    pygame.init()
    pygame.display.set_caption(application_name)
    funcs = {'Start': show_customization,
             'Quit': sys.exit,
             'Settings': show_settings,
             'Credits': show_credits
             }

    gm = GameMenu(funcs)
    gm.run()