import time

from ability_modules import abilities_dictionary
from phase import name
import game_constants
import enemy_data
from items.items_main_functions import items_when_win_battle
from items.gained_items_constants import gained_items_dict


# ------------------------------------------------- If hero won battle and enemy lost battle:
def hero_win_battle(param_fight_level):
    hero_name = name.hero_name
    hero_abilities = abilities_dictionary.abilities
    enemy_abilities = enemy_data.enemies


    time.sleep(1)
    print("\n\n\n------ " + str(hero_name) + " you won the battle! " +
          str(enemy_abilities[param_fight_level]["name"]) + " doesn't have any life to fight more.\n" + game_constants.DIVIDER)
    print("After a victorious battle, your life is: " + str(hero_abilities["Life"]["points"]) +
          "/" + str(game_constants.MAX_LIFE_POINTS))
    time.sleep(2)

    # ----- When the current fight level is lower than the boss fight level:
    if param_fight_level < game_constants.BOSS_FIGHT_LEVEL:
        print("You can take a rest to upgrade your Life points.\n\n" + game_constants.DIVIDER)

        # Increase the available points for customization:
        game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE += param_fight_level

        print("After your win in Level: " + str(param_fight_level) + ", you have " + str(param_fight_level) +
              " extra points to increase your hero abilities. "
              "\nYou can increase your abilities in: \'Menu of the game\' in part: "
              "\'3 - Customize the Hero\'.")
        time.sleep(2)

        # ----------------- So, this phase is about gaining some new Items.
        # 1. Find, if player has an item in gained_items_dict, that has the same Level number as the Level number of currently won battle!
        item_slice_to_list = []
        find_level_number_of_item = ""
        find_item_with_same_level_than_current_level = ""
        for i in gained_items_dict:
            item_slice_to_list = i.split()
            find_level_number_of_item = item_slice_to_list[-1][:-1]
            find_level_number_of_item = int(find_level_number_of_item)
            if find_level_number_of_item == param_fight_level:
                find_item_with_same_level_than_current_level = i

        # 2. If the player has the item from the current won level, then the player skips the phase: items_when_win_battle.
        #    The game gives the hero new extra points for ability increase, but not the possibility to choose some new item.
        if find_item_with_same_level_than_current_level:
            print("\n" + game_constants.DIVIDER)
            print("We found this level number: " + str(param_fight_level) + " in this gained item: " +
                  str(find_item_with_same_level_than_current_level) + ".")
            print("So it means, that you can't to choose another item, from this won level number: " +
                  str(param_fight_level) + " :) ...\n\n")
        # 3. If the player doesn't have the item from the current won level, this phase follows: items_when_win_battle.
        #    The game gives give the hero new extra points for ability increase and the possibility to choose some new item.
        else:
            print("\n" + game_constants.DIVIDER + "\nBut first! After a victorious battle, "
                                                  "you can choose any extra item as a reward.\n\n")
            time.sleep(1)
            items_when_win_battle(param_fight_level)

    time.sleep(2)

    # After gaining or not gaining items, increase the fight level:
    game_constants.FIGHT_LEVEL += 1
