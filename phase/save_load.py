import phase.name
import phase.phase_constants as phase_const
from ability_modules.abilities_dictionary import abilities
import game_constants
from items.gained_items_constants import gained_items_dict
from items import gained_items_constants
from items.items_data import items

import os


def save_game():
    print("------------------------- How do you want to name the saved game?")
    print("Notice!!! The name of the saved game can not contain numbers, special characters or spaces!\n")

    while True:
        user_save_game_input = input("Name of the saved game: ")
        if user_save_game_input.isalpha():
            user_save_game_input.encode(encoding="utf-8")
            break
        else:
            print("------ out of range, try again!\n")
            continue

    if user_save_game_input:
        file_handler_saved_game = open("saved_games/" + user_save_game_input + ".txt", "w", encoding="utf-8")
        # save Hero name
        file_handler_saved_game.write("Hero Name - " + str(phase.name.hero_name) + "\n")

        # save Abilities with Points
        for key in abilities:
            points = str(abilities[key]["points"])
            file_handler_saved_game.write(key + " - " + points + "\n")

        # save Game Phase - check_menu or check_menu_after_fight
        file_handler_saved_game.write("Game Phase - " + str(game_constants.SAVE_PHASE) + "\n")
        # save abilities_points_to_increase which are only at the first start of the game
        file_handler_saved_game.write("points for abilities at the beginning of the game - " +
                                      str(game_constants.ABILITY_POINTS_TO_INCREASE) + "\n")
        # save available_points_to_customize
        file_handler_saved_game.write("Available points to Customize - " + str(game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE) + "\n")
        # save boolean True or False if was first fight or no
        file_handler_saved_game.write("Was there any Fight? - " + str(game_constants.WAS_ANY_FIGHT) + "\n")
        # save Fight Level for choose an enemy monster
        file_handler_saved_game.write("Fight Level - " + str(game_constants.FIGHT_LEVEL) + "\n")

        # save number of gained Items
        file_handler_saved_game.write("Number of Gained Items - " + str(gained_items_constants.number_of_gained_items) + "\n")

        # save gained Items after battles
        if game_constants.WAS_ANY_FIGHT is True:
            for i in gained_items_dict:
                file_handler_saved_game.write(str(i) + "\n")

        file_handler_saved_game.close()

    print("------ Your game is saved with this name: " + str(user_save_game_input))
    print("\n\n")

    return game_constants.SAVE_PHASE


def load_game():
    dict_load_games = {}
    selected_load_game = ""

    # check if EXIST directory saved_games
    if os.path.isdir("saved_games") is False:
        print("------ There are no Saved Games! Start new game!\n")
        return phase_const.START_NEW_GAME

    # check if directory saved_games is EMPTY
    if not os.listdir("saved_games"):
        print("------ There are no Saved Games! Start new game!\n")
        return phase_const.START_NEW_GAME
    else:
        print("------------------------- Which game do you want to load?")
        print("------ You can choose from these saved games:")

        print("0 - Go Back!")

        # create list of saved games
        saved_files = os.listdir("saved_games")

        for i, file in enumerate(saved_files, 1):
            find_txt = file.find(".txt")
            regular_file = file[:find_txt].strip()
            i = str(i)
            print(str(i) + " - " + str(regular_file))
            dict_load_games[i] = regular_file

        while True:
            user_load_game_input = input("------ which game do you want to load: ")

            if user_load_game_input == "0" or user_load_game_input == "Go Back!" or user_load_game_input == "Back":
                return phase_const.INTRO

            if user_load_game_input in dict_load_games.keys() or user_load_game_input in dict_load_games.values():
                if user_load_game_input in dict_load_games.keys():
                    selected_load_game = dict_load_games[user_load_game_input]
                    print("------ You choose this game: " + str(selected_load_game) + "\n")
                elif user_load_game_input in dict_load_games.values():
                    selected_load_game = user_load_game_input
                    print("------ You choose this game: " + str(selected_load_game) + "\n")
            else:
                print("------ out of range, try again!\n")
                continue

            while True:
                print("------ To confirm loaded game \"" + str(selected_load_game) + "\" write 1 or to go back write 0")
                user_load_game_confirm = input("Confirm your selected loaded game: ")

                if user_load_game_confirm == "1":
                    print("------ Let's go to play the game!")
                    print("I'm loading the game under the name: " + str(selected_load_game) + "\n\n")
                    return loading_and_rewriting_game(selected_load_game)
                elif user_load_game_confirm == "0":
                    print("\n")
                    return phase_const.INTRO
                else:
                    print("------ out of range, try again!\n")
                    continue


def loading_and_rewriting_game(selected_game):
    dict_loading_game = {}
    temp_load_dict = {}

    # create dict -> {0: "hero name", 1: "Attack Strength - 1", ... 15: "gained item (LEVEL 4)"}
    file_handler_loading_game = open("saved_games/" + selected_game + ".txt", "r", encoding="utf-8")
    for i, line in enumerate(file_handler_loading_game):
        dict_loading_game[i] = line.strip()

    # load and rewrite Abilities with Points
    for i in range(1, 6+1, 1):
        temp_str = dict_loading_game[i]
        find_dash = dict_loading_game[i].find("-")
        temp_load_dict[temp_str[:find_dash - 1]] = temp_str[find_dash + 1:]

    for key in abilities:
        for k, v in temp_load_dict.items():
            if key == k:
                abilities[key]["points"] = int(v)

    # load and rewrite Hero name
    find_dash = dict_loading_game[0].find("-")
    phase.name.hero_name = dict_loading_game[0][find_dash+2:]

    # load and rewrite Game Phase - check_menu or check_menu_after_fight
    find_dash = dict_loading_game[7].find("-")
    current_phs = dict_loading_game[7][find_dash+2:]

    # load and rewrite abilities_points_to_increase which are only at the first start of the game
    find_dash = dict_loading_game[8].find("-")
    game_constants.ABILITY_POINTS_TO_INCREASE = int(dict_loading_game[8][find_dash+2:])

    # load and rewrite available_points_to_customize
    find_dash = dict_loading_game[9].find("-")
    game_constants.AVAILABLE_POINTS_TO_CUSTOMIZE = int(dict_loading_game[9][find_dash+2:])

    # load and rewrite boolean True or False if was first fight or no
    find_dash = dict_loading_game[10].find("-")
    find_boolean = dict_loading_game[10][find_dash+2:]
    if find_boolean == "False":
        game_constants.WAS_ANY_FIGHT = False
    elif find_boolean == "True":
        game_constants.WAS_ANY_FIGHT = True

    # load and rewrite Fight Level for choose an enemy monster
    find_dash = dict_loading_game[11].find("-")
    game_constants.FIGHT_LEVEL = int(dict_loading_game[11][find_dash+2:])

    # load and rewrite Number of Gained Items
    find_dash = dict_loading_game[12].find("-")
    gained_items_constants.number_of_gained_items = int(dict_loading_game[12][find_dash + 2:])


    # --------- load and rewrite Gained ITEMS in gained_items_dict dict, after win battle ---------
    if gained_items_constants.number_of_gained_items > 0:
        # if we gained any items -> so how many items we gained, so many times this loop does
        for i in range(gained_items_constants.number_of_gained_items):

            # --- 1.part --> find Level number of Gained Item!
            find_level_number_of_item = 0
            temp_split_list = dict_loading_game[13+i].split()
            for j in temp_split_list:
                if ")" in j:
                    find_last_bracket = j.find(")")
                    appended_number = j[:find_last_bracket]
                    if appended_number.isdecimal():
                        find_level_number_of_item = int(appended_number)

            # --- when we have level number of Gained Item:
            # --- 2.part --> find same level number in ITEMS DICT and from its values --> create gained_items_dict
            for x in items[find_level_number_of_item]:
                for k, v in items[find_level_number_of_item][x].items():
                    if v == dict_loading_game[13+i]:
                        gained_items_dict[dict_loading_game[13 + i]] = {}
                        for key, value in items[find_level_number_of_item][x].items():
                            gained_items_dict[dict_loading_game[13 + i]][key] = value
                    break
                if len(gained_items_dict) == (i+1):
                    break


    print("\n------------------------- The game has loaded. Welcome back in game, " + str(phase.name.hero_name) + "!\n\n\n")

    file_handler_loading_game.close()
    return current_phs
