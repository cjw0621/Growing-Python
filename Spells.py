from random import randint

class Spell_m_inv:
    
#Level 1 spell damage    
    heal = str(6)
    pray = str(6)
#Level 2 Spell damage
    fireball = str(randint(1, 6))
    iceball = str(randint(1, 6))
#Level 3 spell damage
    fire_storm = str(randint(2, 12))
    ice_storm = str(randint(2, 12))    
    
#Dict. spell inventory    
    level_1 = {
        "Heal": heal,
        "Pray": pray,
    }
    
    level_2 = {
        "Fireball": fireball,
        "Iceball": iceball,
    } 
       
    level_3 = {
            
        "Fire Storm": fire_storm,
        "Ice Storm": ice_storm,     
    }
    
class Spell_Main:
        
    lvl_1_spells = []
    lvl_1_damage = []
    lvl_2_spells = []
    lvl_2_damage = []
    lvl_3_spells = []
    lvl_3_damage = []

   

    for key, val in Spell_m_inv.level_1.items():
        lvl_1_spells.append(key)
    for key, val in Spell_m_inv.level_1.items():
        lvl_1_damage.append(val)

    for key, val in Spell_m_inv.level_2.items():
        lvl_2_spells.append(key)
    for key, val in Spell_m_inv.level_2.items():
        lvl_2_damage.append(val)

    for key, val in Spell_m_inv.level_3.items():
        lvl_3_spells.append(key)
    for key, val in Spell_m_inv.level_3.items():
        lvl_3_damage.append(val)
        
def sort_lvl1_spellbook(spells, damage):
        
        lvl1_spell_book = []
        
        index_spell = 0
        index_damage = 0
    
        while index_spell < len(Spell_Main.lvl_1_spells):
            sort_spells = spells[index_spell] + ": " + damage[index_damage]
            lvl1_spell_book.append(sort_spells)
            index_spell += 1
            index_damage += 1
            
        return lvl1_spell_book
        
def sort_lvl2_spellbook(spells, damage):
        
        lvl2_spell_book = []
        
        index_spell = 0
        index_damage = 0
    
        while index_spell < len(Spell_Main.lvl_2_spells):
            sort_spells = spells[index_spell] + ": " + damage[index_damage]
            lvl2_spell_book.append(sort_spells)
            index_spell += 1
            index_damage += 1
            
        return lvl2_spell_book   
        
def sort_lvl3_spellbook(spells, damage):
        
        lvl3_spell_book = []
        
        index_spell = 0
        index_damage = 0
    
        while index_spell < len(Spell_Main.lvl_3_spells):
            sort_spells = spells[index_spell] + ": " + damage[index_damage]
            lvl3_spell_book.append(sort_spells)
            index_spell += 1
            index_damage += 1
            
        return lvl3_spell_book                  

class Spell_cast:            

    lvl_1_spellbook = sort_lvl1_spellbook(Spell_Main.lvl_1_spells, Spell_Main.      lvl_1_damage)
            
    lvl_2_spellbook = sort_lvl2_spellbook(Spell_Main.lvl_2_spells, Spell_Main.lvl_2_damage)
            
    lvl_3_spellbook = sort_lvl3_spellbook(Spell_Main.lvl_3_spells, Spell_Main.lvl_3_damage)
    
class Spell_info:
    
    Heal_info = Spell_Main.lvl_1_spells[0] + ": Uses 1 action to cast. You cast a healing light on to yourself that heals a small portion of your health. Heal will also cure any minor ailments."
    
    pray_info = Spell_Main.lvl_1_spells[1] + ": Uses 1 action to cast. You fall on to your knees and recite a prayer that shines down a healing light on you that heals a small portion of your health."


   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    