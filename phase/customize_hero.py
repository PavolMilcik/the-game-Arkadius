from ability_modules.ability_points import ability_points_def
import phase.name
import phase.phase_constants as phase_const
import game_constants
from ability_modules.abilities_dictionary import abilities
from ability_modules.abilities_dictionary import abilities_dict_def
from utils.capitalize_strings import capitalize_input


def customize_hero_001():
    print("------ " + str(phase.name.hero_name) + ", your abilities now look like this:")
    ability_points_def(abilities)

    customize_001_or_back = ["Back", "Customize abilities of Hero"]

    while True:
        print("\n\n------ You have " + str(game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE) + " points to add to your Hero abilities.")
        for i, k in enumerate(customize_001_or_back, 0):
            print(str(i), "-", k)

        customize_check_input_001 = input("------ What will you choose?: ")
        if customize_check_input_001 == "0":
            if game_constants.ABILITY_POINTS_TO_INCREASE <= 0 and game_constants.WAS_ANY_FIGHT is True:
                return phase_const.CHECK_MENU_AFTER_FIGHT
            else:
                print("\n")
                return phase_const.CHECK_MENU
        elif customize_check_input_001 == "1":
            add_or_remove_points_002()
        else:
            print("\tout of the range")



def add_or_remove_points_002():
    while True:
        customize_hero_list = ["Back", "Add points to abilities of Hero(You have " + str(game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE) +
                               " points to add!)", "Remove points from abilities"]

        print("\n")
        for i, k in enumerate(customize_hero_list, 0):
            print(str(i), "-", k)

        customize_check_input_002 = input("------ What will you choose?: ")
        if customize_check_input_002 == "0":
            break
        elif customize_check_input_002 == "1" and game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE == 0:
            print("------ You don't have any points to add!")
        elif customize_check_input_002 == "1" and game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE > 0:
            print("\n\n------ You have " + str(game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE) + " points to add to one of these abilities.")
            add_points_004()
        elif customize_check_input_002 == "2":
            remove_points_003()
        else:
            print("\tout of the range")



def remove_points_003():
    customize_remove_points = ["Go Back!"]
    for i in abilities:
        customize_remove_points.append(i)

    new_abilities_dict_to_remove = {}

    print("\n\n------ " + str(phase.name.hero_name) + ", your abilities now look like this:")
    ability_points_def(abilities)

    print("")
    for i, k in enumerate(customize_remove_points, 0):
        i = str(i)
        print(i, "-", k)
        new_abilities_dict_to_remove[i] = k
    print("7 - Explanation of abilities")


    while True:
        customize_check_input_003 = input("------ Which ability you choose to remove point from?: ")

        # capitalize input
        customize_check_input_003 = capitalize_input(customize_check_input_003)
        if customize_check_input_003 is False:
            print("Please select only the ability that is in the options!\n")
            continue

        # if input is 0 break
        if customize_check_input_003 == "0" or customize_check_input_003 == "Go Back!":
            break
        # if input is 7 so explanation of abilities
        elif customize_check_input_003 == "7" or customize_check_input_003 == "Explanation of abilities" or \
                customize_check_input_003 == "Explanation":
            print("\n------ Explanation of the features of the abilities:")
            abilities_dict_def()
            print("")
            continue
        # if input is in dict and points are >= 1
        elif customize_check_input_003 in new_abilities_dict_to_remove.keys():
            customize_check_input_003 = new_abilities_dict_to_remove[customize_check_input_003]
            if abilities[customize_check_input_003]["points"] >= 1:
                print("\t", customize_check_input_003)
                print("------ You choose this ability: " + customize_check_input_003 + ". I removed point from this ability.")
            else:
                print("------ This ability doesn't have any points to remove!\n")
                continue
        elif customize_check_input_003 in new_abilities_dict_to_remove.values():
            if abilities[customize_check_input_003]["points"] >= 1:
                print("\t", customize_check_input_003)
                print(
                    "------ You choose this ability: " + customize_check_input_003.capitalize() + ". I removed point from this ability.")
            else:
                print("------ This ability doesn't have any points to remove!\n")
                continue
        else:
            print("------ out of range, try again!\n")
            continue

        # remove points from abilities, and add points to var game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE
        if customize_check_input_003 in abilities:
            if abilities[customize_check_input_003]["points"] >= 1:
                if customize_check_input_003 == "Life":
                    abilities[customize_check_input_003]["points"] -= 5
                    game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE += 1
                else:
                    abilities[customize_check_input_003]["points"] -= 1
                    game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE += 1
            else:
                print("------ This ability doesn't have any points to remove!\n")

        # print actual abilities
        print("\n\n------ " + str(phase.name.hero_name) + ", your abilities now look like this:")
        ability_points_def(abilities)

        print("")
        for i, k in enumerate(customize_remove_points, 0):
            i = str(i)
            print(i, "-", k)
            new_abilities_dict_to_remove[i] = k
        print("7 - Explanation of abilities")



def add_points_004():
    customize_add_points = ["Go Back!"]
    for i in abilities:
        customize_add_points.append(i)

    new_abilities_dict_to_add = {}

    print(str(phase.name.hero_name) + ", your abilities now look like this:")
    ability_points_def(abilities)

    print("")
    for i, k in enumerate(customize_add_points, 0):
        i = str(i)
        print(i, "-", k)
        new_abilities_dict_to_add[i] = k
    print("7 - Explanation of abilities")

    while True:
        customize_check_input_004 = input("------ Which ability you choose to add points?: ")

        # capitalize input
        customize_check_input_004 = capitalize_input(customize_check_input_004)
        if customize_check_input_004 is False:
            print("Please select only the ability that is in the options!\n")
            continue

        # if input is 0 break
        if customize_check_input_004 == "0" or customize_check_input_004 == "Go Back!":
            break
        # if input is 7 so explanation of abilities
        elif customize_check_input_004 == "7" or customize_check_input_004 == "Explanation of abilities" or \
                customize_check_input_004 == "Explanation":
            print("\n------ Explanation of the features of the abilities:")
            abilities_dict_def()
            print("")
            continue
        # if input is in dict and points are >= 1
        elif customize_check_input_004 in new_abilities_dict_to_add.keys():
            customize_check_input_004 = new_abilities_dict_to_add[customize_check_input_004]
            # Check if points in the ability 'Life' are not greater than the limit!
            if customize_check_input_004 == "Life" and abilities[customize_check_input_004]["points"] >= game_constants.MAX_LIFE_POINTS:
                print("\n------ IMPORTANT INFORMATION: " + str(game_constants.MAX_LIFE_POINTS) +
                      " is max points for ability LIFE! Try increase another ability.\n")
                continue
            print("\t", customize_check_input_004)
            print("------ You choose this ability: " +
                  customize_check_input_004 + ". I add point, to this ability.")
        elif customize_check_input_004 in new_abilities_dict_to_add.values():
            # Check if points in the ability 'Life' are not greater than the limit!
            if customize_check_input_004 == "Life" and abilities[customize_check_input_004]["points"] >= game_constants.MAX_LIFE_POINTS:
                print("\n------ IMPORTANT INFORMATION: " + str(game_constants.MAX_LIFE_POINTS) +
                      " is max points for ability LIFE! Try increase another ability.\n")
                continue
            print("\t", customize_check_input_004)
            print("------ You choose this ability: " +
                  customize_check_input_004.capitalize() + ". I add point, to this ability.")
        else:
            print("------ out of range, try again!\n")
            continue

        # add points to abilities, and remove points from var game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE
        if customize_check_input_004 in abilities:
            if customize_check_input_004 == "Life":
                abilities[customize_check_input_004]["points"] += 5
                # check and adjust points in Life, if they are bigger than max allowed number of points
                if abilities[customize_check_input_004]["points"] > game_constants.MAX_LIFE_POINTS:
                    print("\n------ IMPORTANT INFORMATION: you have exceeded the limit for LIFE points "
                          "so we must adjust points from: " + str(abilities[customize_check_input_004]["points"]) +
                          " to: " + str(game_constants.MAX_LIFE_POINTS) + " points.")
                    abilities[customize_check_input_004]["points"] = game_constants.MAX_LIFE_POINTS
                game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE -= 1
            else:
                abilities[customize_check_input_004]["points"] += 1
                game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE -= 1

        # end adding points if game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE is 0
        if game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE <= 0:
            print("\n\n------ Sorry, there are no points to add to your abilities!")
            print("------ " + str(phase.name.hero_name) + ", your abilities now look like this:")
            ability_points_def(abilities)
            break

        # print actual abilities and game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE
        print("\n\n------ You have " + str(game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE) + " points to add to one of these abilities.")
        print("------ " + str(phase.name.hero_name) + ", your abilities now look like this:")
        ability_points_def(abilities)

        print("")
        for i, k in enumerate(customize_add_points, 0):
            i = str(i)
            print(i, "-", k)
            new_abilities_dict_to_add[i] = k
        print("7 - Explanation of abilities")
