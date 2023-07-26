def abilities_points_def(param_abilities_dict):
    abilities_dict = param_abilities_dict

    temp_number = 0
    for ability, values in abilities_dict.items():
        print(ability, end="")
        for k, point in values.items():
            if temp_number == len(abilities_dict) - 1:
                print(" - " + str(point))
            else:
                print(" - " + str(point), end=", ")
            temp_number += 1
            break
