import time

import game_constants
import phase.phase_constants as phase_const

from fight.print_stats_battle import print_hero_stats, print_enemy_stats
from fight.simulate_battle import simulate_battle


# ---------------------------------- MAIN Function - of BATTLE ---------------------------
def battle_function(fight_level):

    # hero's scheme of prepared to fight
    print_hero_stats()

    print()
    time.sleep(1)

    # enemy's scheme of prepared to fight
    print_enemy_stats(fight_level)

    time.sleep(2)

    # simulate battle - fight, fight start!
    simulate_battle(fight_level)

    time.sleep(1)

    if fight_level < game_constants.BOSS_FIGHT_LEVEL:
        return phase_const.CHECK_MENU_AFTER_FIGHT
    elif fight_level >= game_constants.BOSS_FIGHT_LEVEL:
        # if in 5 level hero win battle -->
        if game_constants.FIGHT_LEVEL >= game_constants.BOSS_FIGHT_LEVEL:
            return phase_const.WON_GAME
        # when in 5 level hero lose battle -->
        else:
            return phase_const.CHECK_MENU_AFTER_FIGHT
