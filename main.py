# This is the main file of the whole project - the game Arkadius!
import game_constants
import phase.phase_constants as phase_const
import game_constants as game_const
from game_constants import DIVIDER
from phase.intro import intro_game_def, star_new_game_def
from phase.name import name_of_hero_def
from ability_modules.ability_options import ability_options_def
from phase.check_menu import check_menu_def
from phase.customize_hero import customize_hero_001
from phase.save_load import save_game
from phase.save_load import load_game
from fight.battle import battle_function
from phase.check_menu_after_fight import check_menu_after_fight
from phase.won_game import won_game_function


print(DIVIDER + "\n\n\n")
# the phase, when we start the game for the first time:
current_phase = phase_const.INTRO

# here, the phases of the game are changed according to the player's requirements:
while True:
    if current_phase == phase_const.INTRO:
        print("\n" + DIVIDER)
        current_phase = intro_game_def()

    elif current_phase == phase_const.START_NEW_GAME:
        print("\n\n" + DIVIDER)
        current_phase = star_new_game_def()

    elif current_phase == phase_const.END_THE_GAME:
        print(DIVIDER)
        print("------  Alright. The End!")
        print("\t\tSee you next time. ;-)")
        break

    elif current_phase == phase_const.NAME:
        print(DIVIDER)
        current_phase = name_of_hero_def()

    elif current_phase == phase_const.INTRO_ABILITIES:
        print(DIVIDER)
        current_phase = ability_options_def()

    elif current_phase == phase_const.CHECK_MENU:
        print(DIVIDER)
        current_phase = check_menu_def()

    elif current_phase == phase_const.FIGHT:
        print("\n\n" + DIVIDER)
        current_phase = battle_function(game_const.FIGHT_LEVEL)
        game_constants.WAS_ANY_FIGHT = True

    elif current_phase == phase_const.CHECK_MENU_AFTER_FIGHT:
        print("\n\n" + DIVIDER)
        current_phase = check_menu_after_fight()

    elif current_phase == phase_const.CUSTOMIZE_HERO:
        print("\n\n" + DIVIDER)
        print("------------------------- Alright. Customize Hero!\n")
        current_phase = customize_hero_001()

    elif current_phase == phase_const.SAVE_GAME:
        print("\n" + DIVIDER)
        current_phase = save_game()

    elif current_phase == phase_const.LOAD_GAME:
        print(DIVIDER)
        current_phase = load_game()

    elif current_phase == phase_const.WON_GAME:
        print(DIVIDER)
        won_game_function()
        break
