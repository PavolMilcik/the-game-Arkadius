import time

from game_constants import DIVIDER
from phase import name
from abilities_modules.abilities_dictionary import abilities

from items.items_data import items
from items.items_supplementary_functions import items_options_to_choose
from items.items_supplementary_functions import replace_item_or_no
from items.items_supplementary_functions import pop_replaced_item_and_remove_old_points
from items.items_supplementary_functions import item_changed_abilities_points
from items.items_supplementary_functions import write_new_items_to_hero_gained_items
from items.gained_items_constants import gained_items_dict


# ---------------------------------- MAIN Functions - of items, when WIN or LOSE ---------------------------
# if WIN battle, so print new Items to choose:
def print_items_to_choose(param_fight_level, param_item_temp_dict, param_item_temp_list):
    print("You can write number or whole name of item with or without brackets!")

    while True:
        user_item_input = input("Which item you choose?: ")

        # ------ 1.check of user input = NUMBER, check if chosen item is in dict - item_temp_level_dict
        if user_item_input in param_item_temp_dict.keys():
            chosen_new_item_string = param_item_temp_dict[user_item_input]
            chosen_new_item_int = int(user_item_input)
            return chosen_new_item_string, chosen_new_item_int
        # ------ 2.check of user input = ITEM with Bracket, check if chosen item is in dict - item_temp_level_dict
        elif user_item_input in param_item_temp_dict.values():
            chosen_new_item_string = user_item_input
            # find out the number in items dict from user item input
            chosen_new_item_int = 0
            for k, v in param_item_temp_dict.items():
                if v == chosen_new_item_string:
                    chosen_new_item_int = int(k)
            return chosen_new_item_string, chosen_new_item_int
        # ------ 3.check of user input = ITEM without Bracket, check if chosen item is in list - item_temp_level_list
        elif user_item_input in param_item_temp_list:
            # change input to whole string which represents chosen_new_item_string
            chosen_new_item_string = str(user_item_input) + " (LEVEL " + str(param_fight_level) + ")"
            # find out the index number of user item input and +1, because index start from 0!
            chosen_new_item_int = (param_item_temp_list.index(user_item_input)) + 1
            return chosen_new_item_string, chosen_new_item_int
        else:
            print("------ out of range, try again!\n")
            continue


# ---------------------------------- MAIN Functions - of items, when WIN battle ---------------------------
def items_when_win_battle(param_f_level):
    print("\n" + DIVIDER)
    print("You can choose one extra item, which increases your ability points.")
    print("Here are extra items after won battle:")

    # returned new dict and list with items to choose after battle
    item_temp_dict, item_temp_list = items_options_to_choose(param_f_level)

    while True:
        # print items to choose and return chosen item - chosen string and chosen int of item
        chosen_new_item_string, chosen_new_item_int = print_items_to_choose(param_f_level, item_temp_dict, item_temp_list)

        # print chosen item
        print("\n" + str(name.hero_name) + ", you choose this new item: " + chosen_new_item_string)

        # check if item is replaceable
        if items[param_f_level][chosen_new_item_int]["replaceable"] is True and param_f_level > 1:
            replaced_item = replace_item_or_no(chosen_new_item_string, param_f_level)
            if replaced_item is False:
                # if don't want to replace items so: returned new dict and list with items to choose item again
                item_temp_dict, item_temp_list = items_options_to_choose(param_f_level)
                continue
            elif replaced_item:
                # if true, so replace old item with new item.
                pop_replaced_item_and_remove_old_points(replaced_item, chosen_new_item_string)

        # increase or decrease abilities points with chosen item and print points which was increased
        item_changed_abilities_points(param_f_level, chosen_new_item_string, chosen_new_item_int)

        # WRITE GAINED ITEMS to new dict - hero_gained_items
        write_new_items_to_hero_gained_items(param_f_level, chosen_new_item_string)

        break



# ---------------------------------- MAIN Functions - of items, when LOSE battle ---------------------------
# when lose fight, so remove gained item from previous level
# for example, if I go to Fight Level 4

# 1. I lose this battle, so I go back to Fight Level 3
# 2. but first, remove gained item in Fight Level 3, but only those, items which have: "destroy_when_lost": True
#    it means, that only: "tag": "drink", can be lost when we lose battle
# 3. then, we can again fight in Level 3
# 4. and when we again win Fight Level 3 - I can again choose some new item, but only if I lose some item from this Level
# 5. if no, so it means, that I have still any item from Level 3, I can't logical choose any new item!!!
# 5. then go to Fight Level 4

def items_when_lose_battle(param_f_level):

    previous_level = param_f_level - 1

    # find number of item with variable - "destroy_when_lost: True", from previous level
    find_number_of_item = 0
    if len(gained_items_dict) > 0:
        for i in items[previous_level]:
            for k, v in items[previous_level][i].items():
                if k == "destroy_when_lost":
                    find_number_of_item = i
                    break
            if find_number_of_item:
                break

    # find name of item to lose, from previous level
    # item which we are going to remove from gained items
    find_item_to_lost = ""
    if find_number_of_item:
        for k, v in items[previous_level][find_number_of_item].items():
            if k == "name":
                find_item_to_lost = v

    # if we have this item in our dict: gained_items_dict
    # we have to remove it from ours gained items
    removed_item = False
    abilities_to_remove = {}
    if find_item_to_lost:
        for j in gained_items_dict:
            if j == find_item_to_lost:
                for k, v in gained_items_dict[j]["ability"].items():
                    abilities_to_remove[k] = v
                gained_items_dict.pop(j)
                removed_item = True
                break

    # if we removed item from our gained items(gained_items_dict)
    # we have to remove abilities points, which we gained from this item, too
    # so we change actual abilities points
    if removed_item:
        for k, v in abilities_to_remove.items():
            for x in abilities:
                if x == k:
                    abilities[x]["points"] -= v
                    if abilities[x]["points"] < 0:
                        abilities[x]["points"] = 0

    # if we removed item after lost battle, so print something about it
    if removed_item:
        time.sleep(1)
        print(str(name.hero_name) + " after your lost battle, you lose this gained item: " + str(find_item_to_lost) +
              ", from previous Level number: " + str(previous_level) + ".")
        print("You can check all your gained items in: \'Menu of the game\' in part: \'2 - Check gained items\'.")
        print("\n")
    else:
        print(str(name.hero_name) + ", you lost the battle, but there isn't any item to lose from previous Level number: "
              + str(previous_level) + ".\n\n")
