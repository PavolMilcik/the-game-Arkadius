def capitalize_input(input_to_capitalize):

    temp_list = []
    temp_string = ""
        
    if " " in input_to_capitalize:
        find_space = input_to_capitalize.find(" ")
        if find_space == 0 or find_space == len(input_to_capitalize):
            return False
        else:
            temp_list.append(input_to_capitalize[0:find_space])
            temp_list.append(input_to_capitalize[find_space + 1:])
        for i in range(len(temp_list)):
            temp_list[i] = temp_list[i].capitalize()
            if i == len(temp_list) - 1:
                temp_string += temp_list[i]
            else:
                temp_string += temp_list[i] + " "
        input_to_capitalize = temp_string
        return input_to_capitalize
            
    else:
        input_to_capitalize = input_to_capitalize.capitalize()
        return input_to_capitalize
