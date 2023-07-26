import game_constants
from phase import name
from items.gained_items_constants import gained_items_dict

def check_gained_items():
    if len(gained_items_dict) > 1:
        print("------ In this game - Arkadius, you " + str(name.hero_name) + " gained these items:")
        for i in gained_items_dict:
            print(i + " -> ", end="")
            for j in gained_items_dict[i]:
                if j == "description":
                    print(gained_items_dict[i]["description"])
        print("\n\n\n" + game_constants.DIVIDER)
    elif len(gained_items_dict) == 1:
        print("------ In this game - Arkadius, you " + str(name.hero_name) + " gained this item:")
        for i in gained_items_dict:
            print(i + " -> ", end="")
            for j in gained_items_dict[i]:
                if j == "description":
                    print(gained_items_dict[i]["description"])
        print("\n\n\n" + game_constants.DIVIDER)
    elif len(gained_items_dict) == 0:
        print("------ In this game - Arkadius, you " + str(name.hero_name) + " don't have any gained items yet!\n\n")
        print(game_constants.DIVIDER)
