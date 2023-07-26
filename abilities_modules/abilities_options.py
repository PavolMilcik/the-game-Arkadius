import game_constants
from abilities_modules.abilities_points import abilities_points_def
import phase.phase_constants as phase_const
import phase.name
import abilities_modules.abilities_dictionary
from abilities_modules.abilities_dictionary import abilities_dict_def
from game_constants import DIVIDER

def abilities_options_def():
    abilities_dict = abilities_modules.abilities_dictionary.abilities
    name_of_hero = phase.name.hero_name


    print("------------------------- " + str(name_of_hero) + ", your abilities at the beginning of the game look like this:")
    abilities_points_def(abilities_dict)

    print("\n\n" + DIVIDER)
    print("------ At the beginning of the game, you have " +
          str(game_constants.ABILITIES_POINTS_TO_INCREASE) + " points to increase your abilities.")
    print("------ Notice!!!\nOnly for Life ability, 1 point adds 5 points! "
          "For others abilities, 1 point add 1 point to ability.\n")

    while game_constants.ABILITIES_POINTS_TO_INCREASE > 0:
        if game_constants.ABILITIES_POINTS_TO_INCREASE > 1:
            print("\n------------------------- There are still " + str(game_constants.ABILITIES_POINTS_TO_INCREASE) +
                  " points to add to your abilities.")
        else:
            print("\n------------------------- There is still " + str(game_constants.ABILITIES_POINTS_TO_INCREASE) +
                  " point to add to your abilities.")
        print("\nFor explanation of the features of the abilities, write: \n\t0 - Explanation")

        new_choose_ability_dict = {}
        print("You can improve these abilities: ")
        list_abilities_keys = list(abilities_dict.keys())
        for i in range(len(list_abilities_keys)):
            new_choose_ability_dict[str(i+1)] = list_abilities_keys[i]
            print("\t" + str(i+1) + " -", list_abilities_keys[i])

        user_choose_ability_to_increase = input("First, choose an ability to upgrade by adding some points: ")

        if user_choose_ability_to_increase == "0" or user_choose_ability_to_increase == "Explanation":
            print("\n\n------ Explanation of the features of the abilities:")
            abilities_dict_def()
            print("")
            continue

        # capitalize input
        temp_list_001 = []
        temp_string_001 = ""
        if " " in user_choose_ability_to_increase:
            find_space = user_choose_ability_to_increase.find(" ")
            if find_space == 0 or find_space == len(user_choose_ability_to_increase):
                print("Please select only the ability that is in the options!\n")
                continue
            else:
                temp_list_001.append(user_choose_ability_to_increase[0:find_space])
                temp_list_001.append(user_choose_ability_to_increase[find_space + 1:])
            for i in range(len(temp_list_001)):
                temp_list_001[i] = temp_list_001[i].capitalize()
                if i == len(temp_list_001) - 1:
                    temp_string_001 += temp_list_001[i]
                else:
                    temp_string_001 += temp_list_001[i] + " "
            user_choose_ability_to_increase = temp_string_001
        else:
            user_choose_ability_to_increase = user_choose_ability_to_increase.capitalize()

        # if input is str - 1, 2, 3, 4, 5, 6
        if user_choose_ability_to_increase in new_choose_ability_dict.keys():
            user_choose_ability_to_increase = new_choose_ability_dict[user_choose_ability_to_increase]

        # if input is not in abilities
        if user_choose_ability_to_increase not in abilities_dict:
            print("------ Please select only the ability which is in the options!\n")
            continue
        else:
            print("------ You choose " + str(user_choose_ability_to_increase.upper()) + " ability to increase points.")

        # if input is in abilities
        if user_choose_ability_to_increase == "Life":
            if abilities_dict[user_choose_ability_to_increase]["points"] >= game_constants.MAX_LIFE_POINTS:
                print("\n------ IMPORTANT INFORMATION: " + str(game_constants.MAX_LIFE_POINTS) +
                      " is max points for ability LIFE! Try increase another ability.")
                continue
            abilities_dict[user_choose_ability_to_increase]["points"] += 5
            game_constants.ABILITIES_POINTS_TO_INCREASE -= 1
        else:
            abilities_dict[user_choose_ability_to_increase]["points"] += 1
            game_constants.ABILITIES_POINTS_TO_INCREASE -= 1

        print("\n------ Now your abilities points look like this:")
        abilities_points_def(abilities_dict)
        print("")

        if game_constants.ABILITIES_POINTS_TO_INCREASE <= 0:
            break

    print("\n" + DIVIDER)
    print("------------------------- Well done " + str(name_of_hero) +
          ".\nYou finished adding points to your abilities. For recapitulation, your abilities now look like this:")
    abilities_points_def(abilities_dict)
    print("\n\n")

    return phase_const.CHECK_MENU
