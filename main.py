#!/usr/bin/env python
# Include everything here.
import Gameplay
import CustomizationMenu
import SettingsMenu
import CreditsMenu
import sys
from Globals import application_name
import pygame
import MainMenu


def play_game(player1name, player2name, difficulty_easy, sound_on, cheat_code, ship_location):
    sound_on = sound_on[:len(sound_on)-1]
    game = Gameplay.Gameplay(player1name, player2name, ship_location, difficulty_easy, sound_on, cheat_code)
    game.run_game()

if __name__ == "__main__":

    # Creating the screen
    pygame.init()
    pygame.display.set_caption(application_name)
    funcs = {'Start': CustomizationMenu.show_customization,
             'Quit': sys.exit,
             'Settings': SettingsMenu.show_settings,
             'Credits': CreditsMenu.show_credits}

    gm = MainMenu.GameMenu(funcs)
    gm.run()
