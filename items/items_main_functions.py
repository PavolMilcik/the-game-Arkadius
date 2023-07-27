import time

from game_constants import DIVIDER
from phase import name
from ability_modules.abilities_dictionary import abilities

from items.items_data import items
from items.items_supplementary_functions import items_options_to_choose
from items.items_supplementary_functions import replace_item_or_no
from items.items_supplementary_functions import pop_replaced_item_and_remove_old_points
from items.items_supplementary_functions import item_changed_ability_points
from items.items_supplementary_functions import write_new_items_to_gained_items_dict
from items.gained_items_constants import gained_items_dict


# -------------------------- MAIN Functions - of items, when player WON or LOST battle -------------------

# -------------------- if player WON battle, so print new Items to choose:
def print_items_to_choose(param_fight_level, param_item_temp_dict, param_item_temp_list):
    print("You can write number or whole name of item with or without brackets!")

    while True:
        user_item_input = input("Which item you choose?: ")

        # ------ 1.check user input = NUMBER, check if chosen item is in dict - param_item_temp_dict
        if user_item_input in param_item_temp_dict.keys():
            chosen_new_item_string = param_item_temp_dict[user_item_input]
            chosen_new_item_int = int(user_item_input)
            return chosen_new_item_string, chosen_new_item_int
        # ------ 2.check user input = ITEM with Bracket, check if chosen item is in dict - param_item_temp_dict
        elif user_item_input in param_item_temp_dict.values():
            chosen_new_item_string = user_item_input
            # find out the number in param_item_temp_dict dict from user item input
            chosen_new_item_int = 0
            for k, v in param_item_temp_dict.items():
                if v == chosen_new_item_string:
                    chosen_new_item_int = int(k)
            return chosen_new_item_string, chosen_new_item_int
        # ------ 3.check user input = ITEM without Bracket, check if chosen item is in list - param_item_temp_list
        elif user_item_input in param_item_temp_list:
            # change input to whole string which represents chosen_new_item_string
            chosen_new_item_string = str(user_item_input) + " (LEVEL " + str(param_fight_level) + ")"
            # find out the index number of user item input and +1, because index start from 0!
            chosen_new_item_int = (param_item_temp_list.index(user_item_input)) + 1
            return chosen_new_item_string, chosen_new_item_int
        else:
            print("------ out of range, try again!\n")
            continue


# ------------------------------- MAIN Functions - of items, when player WON battle -----------------------
def items_when_win_battle(param_f_level):
    print("\n" + DIVIDER)
    print("You can choose one extra item, which increases your ability points.")
    print("Here are extra items after won battle:")

    # returned new dict and list with items to choose after won battle
    item_temp_dict, item_temp_list = items_options_to_choose(param_f_level)

    while True:
        # print items to choose and return chosen item - chosen string and chosen int/index of item
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

        # increase or decrease ability points with chosen item and print points which was increased
        item_changed_ability_points(param_f_level, chosen_new_item_string, chosen_new_item_int)

        # WRITE GAINED ITEMS to new dict - gained_items_dict
        write_new_items_to_gained_items_dict(param_f_level, chosen_new_item_string)

        break



# ------------------------------- MAIN Functions - of items, when player LOST battle -----------------------

# --- When player lose a fight, remove the gained item from the previous level. 
# For example, if player go to - Fight Level 4, and:
# --- 1. When the player loses a battle in Fight Level 4, player will go back to Fight Level 3.
# --- 2. Then, remove the gained item from the previous fight in Fight Level 3, 
# but only those items which have the designation 'destroy_when_lost': True. 
# It means that only items with the 'tag': 'drink' can be lost when player loses a battle.
# --- 3. Then, the player can once again fight in Level 3.
# --- 4. If the player wins the Fight Level 3 again, player can choose a new item, 
# but only if player lost some item from this Level 3.
# --- 5. If not, it means that the player still has any item from Level 3, 
# so player cannot logically choose any new item!!!
# --- 6. Then the player proceeds to the next level - Fight Level 4.

def items_when_lose_battle(param_f_level):

    previous_level = param_f_level - 1

    # in items from previous level, find the key number of item with this designation - "destroy_when_lost: True"
    find_number_of_item = 0
    if len(gained_items_dict) > 0:
        for i in items[previous_level]:
            for k, v in items[previous_level][i].items():
                if k == "destroy_when_lost":
                    find_number_of_item = i
                    break
            if find_number_of_item:
                break

    # in items from previous level, find the name of item to lose
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
    # so we change actual ability points
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
