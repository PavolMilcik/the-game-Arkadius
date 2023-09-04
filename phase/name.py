import phase.phase_constants as phase_const


hero_name = ""

def name_of_hero_def():
    global hero_name

    while True:
        name_of_hero_input = input("------------------------- Write name for your hero: ")
        name_of_hero_input = name_of_hero_input.capitalize()
        print("------ Hero name: " + str(name_of_hero_input) + "\n\n")
        while True:
            confirm_hero_name_input = input("------ Confirm hero name."
                                            "\n0 - Change name. \n1 - I agree.\nYour choice is: ")
            try:
                confirm_hero_name_input = int(confirm_hero_name_input)
            except ValueError:
                print("Write only integers: 1 or 0!\n")
                continue
            if confirm_hero_name_input != 1 and confirm_hero_name_input != 0:
                print("------ out of range, try again!\n")
                continue
            else:
                break
        if confirm_hero_name_input == 1:
            print("\n------ This is your hero name: " + str(name_of_hero_input) + ".\n\n\n")
            hero_name = name_of_hero_input
            return phase_const.INTRO_ABILITIES
