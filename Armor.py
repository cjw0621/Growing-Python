from random import randint

class ArmorDefense:
    rags = randint(1, 2)
    #Sorcerer
    mage_cloak = randint(2, 5)
    enchanted_mage_cloak = randint(4, 7)
    master_mage_cloak = randint(7, 10)
    dragon_cloak = randint(10, 14)
    #Knight and paladin
    tin_armor = randint(2, 5)
    iron_armor = randint(6, 9)
    steel_armor = randint(8, 11)
    dragon_armor = randint(13, 16)
    #Shields
    round_shield = randint(4, 5)
    kite_shield = randint(5, 6)
    tower_shield = randint(6, 7)