
items = {
    1: {

        1: {
            "name": "Drink of Life (LEVEL 1)",
            "description": "Adds 15 points for ability Life. "
                           "If you die during a fight, your drink will run out. "
                           "You can have several drinks at once.",
            "ability": {
                "Life": 15
            },
            "tag": "drink",
            # it is not replaceable, because - you can have several drinks at once!!!
            "replaceable": False,
            # it is destroyed when you lose battle! because - If you die during a fight, your drink will run out!!!
            "destroy_when_lost": True
        },
        2: {
            "name": "Fabric armor (LEVEL 1)",
            "description": "Adds 2 points for ability Defense. "
                           "You don't lose your fabric armor when you die in the battle, "
                           "as long as you replace it with other armor.",
            "ability": {
                "Defense": 2
            },
            "tag": "armor",
            # it is replaceable, because you can't have several armors at once!!!
            "replaceable": True,
            # it is not destroyed when you lose battle! because it will stay with you until the end of the game,
            # or until you replace it with another armor!!!
            "destroy_when_lost": False
        },
        3: {
            "name": "Simple boots (LEVEL 1)",
            "description": "Adds 1 point for ability Dexterity. "
                           "You don't lose your simple boots when you die in the battle, "
                           "as long as you replace it with other boots.",
            "ability": {
                "Dexterity": 1
            },
            "tag": "boots",
            "replaceable": True,
            "destroy_when_lost": False
        },
    },

    2: {
        1: {
            "name": "Drink of Luck (LEVEL 2)",
            "description": "Adds 5 points for ability Luck. "
                           "If you die during a fight, your drink will run out. "
                           "You can have several drinks at once.",
            "ability": {
                "Luck": 5
            },
            "tag": "drink",
            "replaceable": False,
            "destroy_when_lost": True
        },
        2: {
            "name": "Short sword (LEVEL 2)",
            "description": "Adds 3 points for ability Attack Strength. "
                           "You don't lose your short sword when you die in the battle, "
                           "as long as you replace it with other weapon.",
            "ability": {
                "Attack Strength": 3
            },
            "tag": "weapon",
            "replaceable": True,
            "destroy_when_lost": False
        },
        3: {
            "name": "Gladiator training (LEVEL 2)",
            "description": "Adds 2 points for ability Skill. "
                           "You don't lose your new points for ability Skill when you die in the battle.",
            "ability": {
                "Skill": 2
            },
            "tag": "training",
            "replaceable": False,
            "destroy_when_lost": False
        },
    },

    3: {
        1: {
            "name": "Drink of special Power (LEVEL 3)",
            "description": "Adds 2 points for ability Attack Strength, 2 points for"
                           " ability Defense and 2 points for ability Skill. "
                           "If you die during a fight, your drink will run out. "
                           "You can have several drinks at once.",
            "ability": {
                "Attack Strength": 2,
                "Defense": 2,
                "Skill": 2,
            },
            "tag": "drink",
            "replaceable": False,
            "destroy_when_lost": True
        },
        2: {
            "name": "Long sword (LEVEL 3)",
            "description": "Adds 5 points for ability Attack Strength. "
                           "You don't lose your long sword when you die in the battle, "
                           "as long as you replace it with other weapon.",
            "ability": {
                "Attack Strength": 5
            },
            "tag": "weapon",
            "replaceable": True,
            "destroy_when_lost": False
        },
        3: {
            "name": "Leather boots (LEVEL 3)",
            "description": "Adds 2 points for ability Dexterity and 2 points for ability Defense. "
                           "You don't lose your leather boots when you die in the battle, "
                           "as long as you replace it with other boots.",
            "ability": {
                "Dexterity": 2,
                "Defense": 2,
            },
            "tag": "boots",
            "replaceable": True,
            "destroy_when_lost": False
        },
        4: {
            "name": "Steel armor (LEVEL 3)",
            "description": "Adds 5 points for ability Defense. "
                           "You don't lose your steel armor when you die in the battle, "
                           "as long as you replace it with other armor.",
            "ability": {
                "Defense": 5
            },
            "tag": "armor",
            "replaceable": True,
            "destroy_when_lost": False
        },
    },

    4: {
        1: {
            "name": "Drink of super Energy (LEVEL 4)",
            "description": "Adds 30 points for ability Life a 10 points for ability Luck. "
                           "If you die during a fight, your drink will run out. "
                           "You can have several drinks at once.",
            "ability": {
                "Life": 30,
                "Luck": 10,
            },
            "tag": "drink",
            "replaceable": False,
            "destroy_when_lost": True
        },
        2: {
            "name": "Double sided axe (LEVEL 4)",
            "description": "Adds 10 points for ability Attack Strength. "
                           "You don't lose your double sided axe when you die in the battle, "
                           "as long as you replace it with other weapon.",
            "ability": {
                "Attack Strength": 10
            },
            "tag": "weapon",
            "replaceable": True,
            "destroy_when_lost": False
        },
        3: {
            "name": "Spartan training (LEVEL 4)",
            "description": "Adds 2 points for ability Attack Strength, 2 points for"
                           " ability Defense and 4 points for ability Skill. "
                           "You don't lose your new points for ability Attack Strength, Defense and Skill"
                           " when you die in the battle.",
            "ability": {
                "Attack Strength": 2,
                "Defense": 2,
                "Skill": 4
            },
            "tag": "training",
            "replaceable": False,
            "destroy_when_lost": False
        },
        4: {
            "name": "Roman shield (LEVEL 4)",
            "description": "Adds 16 points for ability Defense, but removes 2 points from ability Dexterity. "
                           "You don't lose your roman shield when you die in the battle, "
                           "as long as you replace it with other armor.",
            "ability": {
                "Defense": 16,
                "Dexterity": -2
            },
            "tag": "armor",
            "replaceable": True,
            "destroy_when_lost": False
        },
    }
}
