import game_constants
from phase import name


def won_game_function():
    print("\n\n\n\n" + game_constants.DIVIDER)
    print(str(name.hero_name) + " you won all battles, you are the best!\nYou have completed the game Arkadius."
                                "\nGood bye and have a nice day... :)\n\n\n\n")
