import phase.phase_constants as phase_const


def intro_game_def():
    print("------------------------- Welcome in the Game - ARKADIUS! \n\tIn this game your Hero will be fighting"
          " against bad and strong Monsters. \n\tThroughout the game, you will be able upgrade skills-abilities of your hero.\n\n")

    start_game_list = ["Start new game", "Load saved game", "End game!"]
    start_game_dict = {}
    while True:
        for i, k in enumerate(start_game_list, 1):
            i = str(i)
            print(i + " - " + k)
            start_game_dict[i] = k

        start_game_input = input("What is your choice?: ")
        start_game_input = start_game_input.capitalize()

        if start_game_input not in start_game_dict.keys() and start_game_input not in start_game_dict.values():
            print("------ out of range, try again!\n")
        elif start_game_input == "1" or start_game_input == "Start new game":
            return phase_const.START_NEW_GAME
        elif start_game_input == "2" or start_game_input == "Load saved game":
            print("\n")
            return phase_const.LOAD_GAME
        elif start_game_input == "3" or start_game_input == "End game!" or start_game_input == "End":
            print("\n")
            return phase_const.END_THE_GAME

def star_new_game_def():

    while True:
        start_new_game_input = input("------------------------- Are you ready to fight?"
                                     "\n0 - No, I am scared.\n1 - Yes, I am ready.\nYour choice is: ")
        try:
            start_new_game_input = int(start_new_game_input)
        except ValueError:
            print("Write only integers: 1 or 0!\n")
            continue
        if start_new_game_input != 1 and start_new_game_input != 0:
            print("------ out of range, try again!\n")
            continue
        elif start_new_game_input == 1:
            print("------ Great. Hero, let's start new game with choosing your name.\n\n")
            return phase_const.NAME
        elif start_new_game_input == 0:
            print("------ Damn, why are you afraid?\n\n")
            return phase_const.END_THE_GAME
