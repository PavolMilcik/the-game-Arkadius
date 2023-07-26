
abilities = {
            "Attack Strength": {
                "points": 1,
                "description": "Strength is needed to attack in battle. For attack you also need dexterity and skill."
            },
            "Defense": {
                "points": 1,
                "description": "Total defense is calculated from defense points + dexterity points."
            },
            "Dexterity": {
                "points": 1,
                "description": "Dexterity is important for defense as well as for attack."
            },
            "Skill": {
                "points": 1,
                "description": "Skill is important for normal attack "
                               "as well as critical attack."
            },
            "Life": {
                "points": 50,
                "description": "Life is important in battle. You can recover your Life after each fight."
            },
            "Luck": {
                "points": 1,
                "description": "Luck is important for critical attack."
            }
        }

def abilities_dict_def():

    for key, value in abilities.items():
        key = key.upper()
        print(str(key) + ":", end=" ")
        for k, v in value.items():
            if k == "description":
                print(str(v))
