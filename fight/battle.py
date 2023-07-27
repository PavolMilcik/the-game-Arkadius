import time

import game_constants
import phase.phase_constants as phase_const

from fight.print_stats_battle import print_hero_stats, print_enemy_stats
from fight.simulate_battle import simulate_battle


# ---------------------------------- MAIN Function of - BATTLE ---------------------------
def battle_function(fight_level):

    # the hero's battle scheme prepared for the fight
    print_hero_stats()

    print()
    time.sleep(1)

    # the enemy's battle scheme prepared for the fight
    print_enemy_stats(fight_level)

    time.sleep(2)

    # battle simulation - fight start!
    simulate_battle(fight_level)

    time.sleep(1)

    # When the current fight level is lower than the boss fight level:
    if fight_level < game_constants.BOSS_FIGHT_LEVEL:
        return phase_const.CHECK_MENU_AFTER_FIGHT
    # When the player is in the last boss fight level:
    elif fight_level >= game_constants.BOSS_FIGHT_LEVEL:
        # and hero win battle -->
        if game_constants.FIGHT_LEVEL >= game_constants.BOSS_FIGHT_LEVEL:
            return phase_const.WON_GAME
        # or hero lose battle -->
        else:
            return phase_const.CHECK_MENU_AFTER_FIGHT
