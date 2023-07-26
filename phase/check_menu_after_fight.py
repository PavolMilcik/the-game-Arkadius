import time
import phase.phase_constants as phase_const
import game_constants
from enemy_data import enemies
from abilities_modules.abilities_dictionary import abilities
from phase.gained_items_check import check_gained_items

def check_menu_after_fight():
    print("------------------------- Menu of the game:")

    check_menu_list = ["Take a rest to upgrade Life by 20 points. Your Life has now: " +
                       str(abilities["Life"]["points"]) + "/" + str(game_constants.MAX_LIFE_POINTS) + " points.",
                       "Start the Fight against: " + str(enemies[game_constants.FIGHT_LEVEL]["name"]),
                       "Check gained Items", "Customize the Hero", "Save the Game", "End the Game"]
    check_menu_list = enumerate(check_menu_list, 0)
    check_menu_dict = dict(check_menu_list)

    check_menu_dict = {str(k): v for k, v in check_menu_dict.items()}

    while True:

        for k, v in check_menu_dict.items():
            k = str(k)
            print(k + " -", v)

        check_input = input("What is your next step?: ")

        # check for " " in user input
        if " " in check_input:
            temp_string = ""
            temp_list = []
            temp_it = 0
            for i in check_input:
                temp_it += 1
                if i != " " and i != "\n":
                    temp_string += i
                if i == " " or i == "\n" or temp_it == len(check_input):
                    temp_list.append(temp_string)
                    temp_string = ""

            new_string_input = ""
            for j in range(len(temp_list)):
                if j == 0 or j == len(temp_list) - 1:
                    temp_list[j] = temp_list[j].capitalize()
                    new_string_input += temp_list[j]
                else:
                    temp_list[j] = temp_list[j].lower()
                    new_string_input += temp_list[j] + " "
                if j == 0:
                    new_string_input += " "
            check_input = new_string_input

        # when user choose, return will be...
        if check_input in check_menu_dict.keys() or check_input in check_menu_dict.values():
            if check_input == "0" or check_input == "Take a rest":
                print("\n------ You choose: 0 - Take a rest to upgrade Life by 20 points.\n")
                time.sleep(2)
                if abilities["Life"]["points"] < game_constants.MAX_LIFE_POINTS:
                    print("Good choice, take a rest and breathe well. Here are 20 points for your ability Life.")
                    abilities["Life"]["points"] += 20
                    if abilities["Life"]["points"] > game_constants.MAX_LIFE_POINTS:
                        abilities["Life"]["points"] = game_constants.MAX_LIFE_POINTS
                else:
                    print("------ Error! You have max Life points, there's no way to take a rest to upgrade Life points!")
                print("------ Your Life has now: " + str(abilities["Life"]["points"]) + "/" +
                      str(game_constants.MAX_LIFE_POINTS) + " points.\n")
                return phase_const.CHECK_MENU_AFTER_FIGHT

            elif check_input == "1" or check_input == "Start the Fight":
                print("\n------ You choose: 1 - Start the Fight against: " + str(enemies[game_constants.FIGHT_LEVEL][
                    "name"]) + "\n")
                return phase_const.FIGHT

            elif check_input == "2" or check_input == "Check gained items":
                print("\n\n\n------ You choose: 2 - Check gained items\n\n")
                check_gained_items()
                time.sleep(2)


            elif check_input == "3" or check_input == "Customize the Hero":
                print("\n------ You choose: 3 - Customize the Hero\n")
                return phase_const.CUSTOMIZE_HERO

            elif check_input == "4" or check_input == "Save the Game":
                if game_constants.WAS_ANY_FIGHT is True:
                    game_constants.SAVE_PHASE = phase_const.CHECK_MENU_AFTER_FIGHT
                print("\n------ You choose: 4 - Save the Game\n")
                return phase_const.SAVE_GAME

            elif check_input == "5" or check_input == "End the Game":
                print("\n------ You choose: 5 - End the Game\n")
                print("\n------------------------- Are you sure, that you want to end the game?")
                end_check_list = ["Back", "End the Game."]
                while True:
                    for i, k in enumerate(end_check_list):
                        print(str(i) + " -", k)
                    user_input = input("Really?! End the game?: ")
                    if user_input == "0":
                        print("I knew it :D")
                        print("\n")
                        break
                    elif user_input == "1":
                        print("\n")
                        return phase_const.END_THE_GAME
                    else:
                        print("------ out of range, try again!\n")
        else:
            print("------ out of range, try again!\n")
            continue
