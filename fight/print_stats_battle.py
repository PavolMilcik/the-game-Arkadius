from ability_modules import abilities_dictionary
from phase import name
import enemy_data

from fight.values_of_attack_defense import hero_fight_value, enemy_fight_value


# ----------------------- Print the hero's and the enemy's battle scheme prepared for the fight. ----------------
def print_hero_stats():
    hero_name = name.hero_name
    hero_abilities = abilities_dictionary.abilities

    hero_attack_min, hero_attack_max, hero_defense_min, hero_defense_max, hero_critical_attack = hero_fight_value()

    print("Hero: " + str(hero_name) + " goes to the battle prepared as follows:")
    print("Attack: min - " + str(hero_attack_min) + ", max - " + str(hero_attack_max))
    print("Critical attack chance is - " + str(hero_critical_attack) + "%")
    print("Defense: min - " + str(hero_defense_min) + ", max - " + str(hero_defense_max))
    print("Life - " + str(hero_abilities["Life"]["points"]))


def print_enemy_stats(fight_level):
    enemy_abilities = enemy_data.enemies
    enemy_life = enemy_abilities[fight_level]["Life"]

    enemy_attack_min, enemy_attack_max, enemy_defense_min, enemy_defense_max, enemy_critical_attack = enemy_fight_value(fight_level)

    print("Your enemy: " + str(enemy_abilities[fight_level]["name"]) +
          " goes to the battle prepared as follows:")
    print("Attack: min - " + str(enemy_attack_min) + ", max - " + str(enemy_attack_max))
    print("Critical attack chance is - " + str(enemy_critical_attack) + "%")
    print("Defense: min - " + str(enemy_defense_min) + ", max - " + str(enemy_defense_max))
    print("Life - " + str(enemy_life))
