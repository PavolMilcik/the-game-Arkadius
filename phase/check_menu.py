import phase.phase_constants as phase_const
import game_constants
from enemy_data import enemies


def check_menu_def():
    print("------------------------- Menu of the game:")

    check_menu_list = ["Start the Fight against: " + enemies[game_constants.FIGHT_LEVEL]["name"],
                       "Customize the Hero", "Save the Game", "End the Game"]
    check_menu_list = enumerate(check_menu_list, 1)
    check_menu_dict = dict(check_menu_list)
    # print(check_menu_dict)

    # new_dict = {}
    # for k, v in check_menu_dict.items():
    #     new_dict[str(k)] = v
    # print(new_dict)

    check_menu_dict = {str(k): v for k, v in check_menu_dict.items()}
    # print(check_menu_dict)

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
            if check_input == "1" or check_input == "Start the Fight":
                print("\n------ You choose: 1 - Start the Fight against: " + enemies[game_constants.FIGHT_LEVEL]["name"] + "\n")
                return phase_const.FIGHT
            elif check_input == "2" or check_input == "Customize the Hero":
                print("\n------ You choose: 2 - Customize the Hero\n")
                return phase_const.CUSTOMIZE_HERO
            elif check_input == "3" or check_input == "Save the Game":
                if game_constants.WAS_ANY_FIGHT is True:
                    game_constants.SAVE_PHASE = phase_const.CHECK_MENU_AFTER_FIGHT
                else:
                    game_constants.SAVE_PHASE = phase_const.CHECK_MENU
                print("\n------ You choose: 3 - Save the Game\n")
                return phase_const.SAVE_GAME
            elif check_input == "4" or check_input == "End the Game":
                print("\n------ You choose: 4 - End the Game\n")
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
