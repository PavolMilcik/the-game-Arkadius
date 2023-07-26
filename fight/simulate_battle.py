import random
import time

from abilities_modules import abilities_dictionary
from phase import name
import enemy_data
import game_constants

from fight.values_of_attack_defense import hero_fight_value, enemy_fight_value, is_critical_hit
from fight.hero_lose import hero_lose_battle
from fight.hero_win import hero_win_battle


# ---------------------------------- 3.Supplementary Functions - of BATTLE ---------------------------
def simulate_battle(fight_level):
    hero_name = name.hero_name
    hero_abilities = abilities_dictionary.abilities
    enemy_abilities = enemy_data.enemies
    enemy_life = enemy_abilities[fight_level]["Life"]

    hero_attack_min, hero_attack_max, hero_defense_min, hero_defense_max, hero_critical_attack = hero_fight_value()
    enemy_attack_min, enemy_attack_max, enemy_defense_min, enemy_defense_max, enemy_critical_attack = enemy_fight_value(fight_level)

    print(game_constants.DIVIDER)
    print("------ Battle starts! You - " + str(hero_name) + " attack first.\n")

    # --------------------------------------- battle - attacks start
    while True:
        # hero random attack and random defense
        hero_random_attack = random.randint(hero_attack_min, hero_attack_max)
        hero_random_defense = random.randint(hero_defense_min, hero_defense_max)

        # enemy random attack and random defense
        enemy_random_attack = random.randint(enemy_attack_min, enemy_attack_max)
        enemy_random_defense = random.randint(enemy_defense_min, enemy_defense_max)

        # hero attack
        if enemy_life > 0 and hero_abilities["Life"]["points"] > 0:
            time.sleep(1)
            if is_critical_hit(hero_critical_attack):
                print("Critical attack is used by Hero!")
                hero_random_attack *= 3
            total_hero_attack = hero_random_attack - enemy_random_defense
            if total_hero_attack > 0:
                print(str(hero_name) + " you attack the enemy with this attack power: " + str(total_hero_attack))
                enemy_life -= total_hero_attack
                print("After your attack " + str(enemy_abilities[fight_level]["name"]) +
                      " life is: " + str(enemy_life) + "\n")
            else:
                print("Enemy's defense was stronger than your attack, your attack missed the opponent.\n")
        else:
            break

        # enemy attack
        if hero_abilities["Life"]["points"] > 0 and enemy_life > 0:
            time.sleep(1)
            if is_critical_hit(enemy_critical_attack):
                print("Critical attack is used by Enemy!")
                enemy_random_attack *= 3
            total_enemy_attack = enemy_random_attack - hero_random_defense
            if total_enemy_attack > 0:
                print(str(enemy_abilities[fight_level]["name"]) + " attacks you with this attack power: " +
                      str(total_enemy_attack))
                hero_abilities["Life"]["points"] -= total_enemy_attack
                print("After enemy's attack your life is: " + str(hero_abilities["Life"]["points"]) + "\n")
            else:
                print("Hero, your defense was stronger than enemy's attack, enemy's attack missed you.\n")
        else:
            break


    # ------- after attacks, after battle
    # if hero lose and enemy win
    if hero_abilities["Life"]["points"] <= 0:
        hero_lose_battle(fight_level)

    # if hero win and enemy lose
    elif enemy_life <= 0:
        hero_win_battle(fight_level)
