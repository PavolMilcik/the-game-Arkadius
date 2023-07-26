import time

from abilities_modules import abilities_dictionary
from phase import name
import game_constants
import enemy_data
from items.items_main_functions import items_when_win_battle
from items.gained_items_constants import gained_items_dict

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

    # ----- when fight level is lower than boss fight level
    if param_fight_level < game_constants.BOSS_FIGHT_LEVEL:
        print("You can take a rest to upgrade your Life points.\n\n" + game_constants.DIVIDER)

        # increase available points to customize
        game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE += param_fight_level

        print("After your win in Level: " + str(param_fight_level) + ", you have " + str(param_fight_level) +
              " extra points to increase your hero abilities. "
              "\nYou can increase your abilities in: \'Menu of the game\' in part: "
              "\'3 - Customize the Hero\'.")
        time.sleep(2)

        # ----------------- so this phase is about gain some new Items ?!
        # 1. find if we have gained items in gained_items_dict, with same Level number, like is Level number of win battle!
        item_slice_to_list = []
        find_level_number_of_item = ""
        find_item_with_same_level_than_current_level = ""
        for i in gained_items_dict:
            item_slice_to_list = i.split()
            find_level_number_of_item = item_slice_to_list[-1][:-1]
            find_level_number_of_item = int(find_level_number_of_item)
            if find_level_number_of_item == param_fight_level:
                find_item_with_same_level_than_current_level = i

        # 2. if we have some gained item from current level, we skip phase: items_when_win_battle
        # we give hero some new extra points for abilities increase, but not possibility to choose some new item
        if find_item_with_same_level_than_current_level:
            print("\n" + game_constants.DIVIDER)
            print("We found this level number: " + str(param_fight_level) + " in this gained item: " +
                  str(find_item_with_same_level_than_current_level) + ".")
            print("So it means, that you can't to choose another item, from this won level number: " +
                  str(param_fight_level) + " :) ...\n\n")
        # 3. if we haven't some gained item from current level, this phase follows: items_when_win_battle
        # we give hero some new extra points for abilities increase and possibility to choose some new item
        else:
            print("\n" + game_constants.DIVIDER + "\nBut first! After a victorious battle, "
                                                  "you can choose any extra item as a reward.\n\n")
            time.sleep(1)
            items_when_win_battle(param_fight_level)

    time.sleep(2)

    # after gained or not gained items: increase fight level
    game_constants.FIGHT_LEVEL += 1
