import random

import enemy_data
from abilities_modules import abilities_dictionary


# ---------------------------------- 1.Supplementary Functions - of BATTLE ---------------------------
def hero_fight_value():
    hero_abilities = abilities_dictionary.abilities

    # ------------------- hero values
    hero_attack_min = hero_abilities["Attack Strength"]["points"]
    hero_attack_max = hero_abilities["Attack Strength"]["points"] + \
                      hero_abilities["Dexterity"]["points"] + \
                      hero_abilities["Skill"]["points"]

    hero_defense_min = hero_abilities["Defense"]["points"]
    hero_defense_max = hero_abilities["Defense"]["points"] + \
                       hero_abilities["Dexterity"]["points"]

    # min - return number which is not bigger than 100
    # // - round number to down, from this 9//2=4.5 return 4
    hero_critical_attack = min(100, (hero_abilities["Skill"]["points"] * hero_abilities["Luck"]["points"]) // 2)

    return hero_attack_min, hero_attack_max, hero_defense_min, hero_defense_max, hero_critical_attack


def enemy_fight_value(fight_level):
    enemy_abilities = enemy_data.enemies

    # ------------------- enemy values
    enemy_attack_min = enemy_abilities[fight_level]["Attack Strength"]
    enemy_attack_max = enemy_abilities[fight_level]["Attack Strength"] + \
                       enemy_abilities[fight_level]["Dexterity"] + \
                       enemy_abilities[fight_level]["Skill"]

    enemy_defense_min = enemy_abilities[fight_level]["Defense"]
    enemy_defense_max = enemy_abilities[fight_level]["Defense"] + \
                        enemy_abilities[fight_level]["Dexterity"]

    # min - return number which is not bigger than 100
    # // - round number to down, from this 9/2=4.5 return 4
    enemy_critical_attack = min(100, (enemy_abilities[fight_level]["Skill"] * enemy_abilities[fight_level]["Luck"]) // 2)

    return enemy_attack_min, enemy_attack_max, enemy_defense_min, enemy_defense_max, enemy_critical_attack


def is_critical_hit(chance):
    return random.randint(0, 100) < chance
