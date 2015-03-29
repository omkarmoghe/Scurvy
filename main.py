# Include everything here.
from Globals import *
import Gameplay
from MainMenu import *


def play_game(player1name, player2name, difficulty_easy, sound_on, cheat_code):
    # print "Player 1 name: " + player1name
    # print "Player 2 name: " + player2name
    # print "easy: "
    # print difficulty_easy
    sound_on = sound_on[:len(sound_on)-1]
    # print "sound on: " + sound_on
    # print "cheat: " + cheat_code
    game = Gameplay.Gameplay(player1name, player2name, classic_ship_location, difficulty_easy, sound_on, cheat_code)
    game.run_game()

if __name__ == "__main__":
    # Creating the screen
    pygame.init()
    pygame.display.set_caption(application_name)
    funcs = {'Start': show_customization,
             'Quit': sys.exit,
             'Settings': show_Settings,
             'Credits': show_Credits
             }

    gm = GameMenu(funcs)
    gm.run()