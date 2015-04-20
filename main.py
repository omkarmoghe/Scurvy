#!/usr/bin/env python
# Include everything here.
import Gameplay
import CustomizationMenu
import SettingsMenu
import CreditsMenu
import sys
import TutorialMenu
from Globals import application_name
import pygame
import MainMenu


def play_game(player1name, player2name, difficulty_easy, music_on, sfx_on, cheat_code, ship_location):
    music_on = music_on[:len(music_on)-1]
    sfx_on = sfx_on[:len(sfx_on)-1]
    game = Gameplay.Gameplay(player1name, player2name, ship_location, difficulty_easy, music_on, sfx_on, cheat_code)
    game.run_game()

if __name__ == "__main__":

    # Creating the screen
    pygame.init()
    pygame.display.set_caption(application_name)
    funcs = {'Start': CustomizationMenu.show_customization,
             'Quit': sys.exit,
             'Settings': SettingsMenu.show_settings,
             'Tutorial': TutorialMenu.show_tutorial,
             'Credits': CreditsMenu.show_credits}

    gm = MainMenu.GameMenu(funcs)
    gm.run()
