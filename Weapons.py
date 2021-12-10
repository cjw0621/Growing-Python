from random import randint

class WeaponHit:
    
    crit = randint(1, 100)
    
    if crit >= 85:
        crit = 10
    elif crit <= 85:
        crit = 0  
            
    f_class = randint(0 ,2)
    c_class = randint(2 ,5)
    c_class = c_class + crit
    b_class = randint(4, 7)
    b_class = b_class + crit
    a_class = randint(5, 9)
    a_class = a_class + crit
    s_class = randint(6, 12)
    s_class = s_class + crit
            
class WeaponClass:
    #Knight and paladin weapons
    broadsword = WeaponHit.c_class
    shortsword = WeaponHit.c_class
    black_sword = WeaponHit.b_class
    enchanted_long_sword = WeaponHit.a_class 
    dragon_scimetar = WeaponHit.s_class 
    #Sorcerers weapons
    staff = WeaponHit.c_class - WeaponHit.crit
    curved_staff = WeaponHit.b_class - WeaponHit.crit
    enchanted_staff = WeaponHit.a_class - WeaponHit.crit
    dragon_staff = WeaponHit.s_class - WeaponHit.crit
    #Peasant weapons
    wood_sword = WeaponHit.f_class


    

    
