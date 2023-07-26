import time

from abilities_modules import abilities_dictionary
from phase import name
import game_constants
from items.items_main_functions import items_when_lose_battle



def hero_lose_battle(param_fight_level):
    hero_name = name.hero_name
    hero_abilities = abilities_dictionary.abilities

    time.sleep(1)
    print("\n\n\n------ " + str(hero_name) + " you lost the battle!\n" + game_constants.DIVIDER)
    print("Your life points score is: " + str(hero_abilities["Life"]["points"]) + "/" +
          str(game_constants.MAX_LIFE_POINTS))

    print("You don't have any Life to fight with enemy." +
          "\nYou need to take a rest to upgrade your Life points and then you can change abilities points.\n")
    print(game_constants.DIVIDER)

    # here going phase when we lose battle
    if param_fight_level > 1:
        # so this phase is about lose some gained Items
        items_when_lose_battle(param_fight_level)

        time.sleep(1)
        # decrease Level of Fights
        game_constants.FIGHT_LEVEL -= 1
