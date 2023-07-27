from ability_modules.abilities_dictionary import abilities
import game_constants

from items.items_data import items
from items.gained_items_constants import gained_items_dict
from items import gained_items_constants


# ---------------------- Supplementary Functions - of items, when player WON or LOST battle ----------------

def items_options_to_choose(param_level):
    # item_temp_level_dict = { 1: "Drink of Life (LEVEL 1)", 2: "Fabric armor (LEVEL 1)", ... }
    # item_temp_level_list = [Drink of Life, Fabric armor, ...]
    item_temp_level_dict = {}
    item_temp_level_list = []

    # print items to choose from and their descriptions in the current round
    for i in items[param_level]:
        for k, v in items[param_level][i].items():
            if k == "name":
                print(str(i) + " - " + str(v) + " -> ", end="")
                # write items to new dict with bracket
                item_temp_level_dict[str(i)] = v
                # write items to new list without bracket
                find_bracket = v.find("(")
                item_temp_level_list.append(v[:find_bracket-1])
            if k == "description":
                print(str(v))

    print("")
    # after battle, return new dict and list with items to choose
    return item_temp_level_dict, item_temp_level_list


def replace_item_or_no(param_chosen_item, param_level):
    # actual tag of chosen item
    actual_tag = ""
    for i in items[param_level]:
        for j in items[param_level][i].values():
            if j == param_chosen_item:
                actual_tag = items[param_level][i]["tag"]

    # is it replaceable item with same tag in gained_items_dict?
    # if yes, create variable item_to_replace
    item_to_replace = ""
    for i in gained_items_dict:
        for j in gained_items_dict[i].values():
            if j == actual_tag:
                item_to_replace = i

    # if exist item_to_replace
    if item_to_replace:
        print("You already have one type of " + str(actual_tag) +
              ", do you want to replace it with this " + str(actual_tag) + ", or do you want to choose another item?\n")
        print("0 - Back to choose another item.\n"
              "1 - Replace old " + str(actual_tag) + ": " + str(item_to_replace) +
              ", with new " + str(actual_tag) + ": " + str(param_chosen_item) + "!")

        # while loop - to replace or choose new item
        while True:
            user_replaceable_input = input("What do you choose?: ")
            if user_replaceable_input == "0":
                print("\n\n------ You don't want to replace old item with new item, you want to choose another item.\n")
                return False
            elif user_replaceable_input == "1":
                print("\n\n------ Ok, you want to replace old item with new item.")
                return item_to_replace
            else:
                print("------ out of range, try again!\n")
                continue


def pop_replaced_item_and_remove_old_points(param_replaced_item, param_new_item):
    # remove ability points of replaced item from hero ability points
    abilities_and_points_to_remove = {}
    for k, v in gained_items_dict[param_replaced_item]["ability"].items():
        abilities_and_points_to_remove[k] = v

    for k, v in abilities_and_points_to_remove.items():
        for i in abilities:
            if i == k:
                abilities[i]["points"] -= v
                if abilities[i]["points"] < 0:
                    abilities[i]["points"] = 0

    print(str(param_replaced_item) + " was removed from your bag: \'gained items\'.")
    print("It was replaced with: " + str(param_new_item) + ".")
    # pop replaced item from gained items dict
    gained_items_dict.pop(param_replaced_item)



def adjust_life_points():
    if abilities["Life"]["points"] > game_constants.MAX_LIFE_POINTS:
        print("\n------ IMPORTANT INFORMATION: you have exceeded the limit of LIFE points "
              "so we must adjust points from: " + str(abilities["Life"]["points"]) +
              " to: " + str(game_constants.MAX_LIFE_POINTS) + " points.")
        abilities["Life"]["points"] = game_constants.MAX_LIFE_POINTS


def item_changed_ability_points(param_level, param_chosen_new_item, param_chosen_new_item_int):
    # variable - integer, in which part of current level - is ability to increase or decrease
    find_ablts_in_chosen_item = int()
    for i in items[param_level]:
        for k, v in items[param_level][i].items():
            if param_chosen_new_item == v:
                find_ablts_in_chosen_item = i

    # specific abilities to increase or decrease
    ablts_to_change = {}
    for k, v in items[param_level][find_ablts_in_chosen_item]["ability"].items():
        ablts_to_change[k] = v

    # increase or decrease ability points with chosen item
    for k, v in ablts_to_change.items():
        for i in abilities:
            if k == i:
                abilities[i]["points"] += v
                if abilities[i]["points"] < 0:
                    abilities[i]["points"] = 0

    # print ability points which was increased
    for k, v in items[param_level][param_chosen_new_item_int]["ability"].items():
        if v > 0:
            print(" -> this item gives you: " + str(v) + " points for ability: " + str(k))
        else:
            print(" -> this item removes: " + str(v) + " points from your ability: " + str(k))
    print("Your abilities were upgraded! Check it in: \'Menu of the game\' in part: \'3 - Customize the Hero\' \n\n")

    # if Life points are greater than 60 points
    adjust_life_points()


def write_new_items_to_gained_items_dict(param_f_level, chosen_new_item_string):
    # WRITE GAINED ITEMS to new dict - gained_items_dict
    for i in items[param_f_level]:
        for k, v in items[param_f_level][i].items():
            if v == chosen_new_item_string:
                gained_items_dict[chosen_new_item_string] = {}
                for key, value in items[param_f_level][i].items():
                    gained_items_dict[chosen_new_item_string][key] = value
                break

    # number of gained items
    gained_items_constants.number_of_gained_items = len(gained_items_dict)
