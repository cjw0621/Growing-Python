import class_main as main

print("Welcome to my first ever text based adventure.\nBefore we start what class do you wish to be?\nYou may choose from either a Paladin, a Knight, a Sorcerer, or a Peasent.")


user_class = 0

while True:
      
      char_class = input("\nType here -> ")
      
      if char_class == "paladin" or char_class == "Paladin":
          user_class =("Paladin")
          y_n = input("Excellent, are you sure you want to choose this class?\nType here -> ")
          if y_n == "y" or y_n == "yes" or y_n == "Yes" or y_n == "Y" or y_n == "yea" or y_n == "Yea":
             break
          elif y_n == "n" or y_n == "no" or y_n == "No" or y_n == "N" or y_n == "nah" or y_n == "Nah":
             print("Then choose carefully next time. Which class do you wish to be?")
             
      elif char_class == "knight" or char_class == "Knight":
          user_class = ("Knight")
          y_n = input("Excellent, are you sure you want to choose this class?\nType here -> ")
          if y_n == "y" or y_n == "yes" or y_n == "Yes" or y_n == "Y" or y_n == "yea" or y_n == "Yea":
             break
          elif y_n == "n" or y_n == "no" or y_n == "No" or y_n == "N" or y_n == "nah" or y_n == "Nah":
             print("Then choose carefully next time. Which class do you wish to be?")
             
      elif char_class == "sorcerer" or user_class == "Sorcerer":
          user_class = ("Sorcerer")
          y_n = input("Excellent, are you sure you want to choose this class?\nType here -> ")
          if y_n == "y" or y_n == "yes" or y_n == "Yes" or y_n == "Y" or y_n == "yea" or y_n == "Yea":
             break
          elif y_n == "n" or y_n == "no" or y_n == "No" or y_n == "N" or y_n == "nah" or y_n == "Nah":
             print("Then choose carefully next time. Which class do you wish to be?")
      elif char_class == "peasent" or char_class == "Peasent":
          user_class = ("Peasent")
          y_n = input("Excellent, are you sure you want to choose this class?\nType here -> ")          
          if y_n == "y" or y_n == "yes" or y_n == "Yes" or y_n == "Y" or y_n == "yea" or y_n == "Yea":
             break
          elif y_n == "n" or y_n == "no" or y_n == "No" or y_n == "N" or y_n == "nah" or y_n == "Nah":
             print("Then choose carefully next time. Which class do you wish to be?")
             
      else:
          print("\n Please choose a class.")


input("\nPush enter to continue...\n")

print("Chapter 1: The begining\n")
print("\nNarrator: It has been a long journey to adulthood for you young " + user_class + ". Your parents died, burned alive in a catastrophic village fire. You were just a young child at the time. You can still smell the burning corpse of your fellow villagers. Alone and afraid you ran towards the great unknown.\n ")

input("\nPush enter to continue...\n")

print("\nNarrator: You ran for what felt like centries. You ran until you reached a cottege. As curious as curious comes, you approached the cottege. The area smelled heavenly. The area smells of baked duck, roasted pork, and lamb stew. With an appetite worked up from all the running, you became desperate for food. You knocked on the door...\n")

input("\nPush enter to continue...\n")















#use for the player to add spells to their spellbook
player_spells = []

loop = True

print("\nPeaty: In my book are secrets to unlock unlimited power. One day, when you are fully trained in the art of spell casting, you too may learn this knowledge. However, given that you are new to this relm, the power inside you is still growing. So to start you off on your journey you may pick one level 1 and one level 2 spell from my book.\nThese spells are\nLevel 1: " + str(main.lvl_1_spell) + "\nLevel 2: " + str(main.lvl_2_spell) + "\n\nWhich level 1 spell do you choose?\n")

while loop:
    user_input = input("Type here --> ")

    if user_input == "heal" or user_input == ("Heal"):
        player_spells.append("Heal")
        if player_spells[0] == "Heal":
            print("System: Your spellbook now contains " + player_spells[0] + "\n")
            break                            
    elif user_input == "Pray" or user_input == ("pray"):
        player_spells.append("Pray")
        if player_spells[0] == "Pray":
            print("System: Your spellbook now contains " + player_spells[0] + "\n")
            break
    elif user_input == "fireball" or user_input == "Fireball" or user_input == "iceball" or user_input == "Iceball":
        print("\nPeaty: Adventurer, you must choose a level 1 spell first.")
    else:
        print("\nPeaty: Adventurer, that was gibberish, I have no idea as to what you just said. \nPick a spell already! I don't have all day!\n")

print("\nPeaty: Excellent! Now choose a level 2 spell you want to add into your spellbook.\n")

while loop:
     user_input = input("\nType here --> ")
     
     if user_input == "fireball" or user_input == "Fireball":
         player_spells.append("Fireball")
         print("System: Your spellbook now contains " + player_spells[0] + " and " + player_spells[1] + ".")
         break
     elif user_input == "iceball" or user_input == "Iceball":
         player_spells.append("Iceball")
         print("System: Your spellbook now contains " + player_spells[0] + " and " + player_spells[1] + ".")
         break
     elif user_input == "pray" or user_input == "Pray":
         if player_spells[0] == "Pray":
             print("Peaty: Adventurer, you cant add pray because you ALREADY HAVE PRAY! Please tell me you aren't an idiot and you're just trying my patience...on another thought, don't tell me. Just tell me what level 2 spell you want to add to your spellbook.")
         elif player_spells[0] == "Heal":
             print("Peaty: Now, now, now, dont get greedy so early in the game adventurer. For you can only have ONE level 1 spell in your spellbook. Since you have already picked one, you must now pick a level 2 spell. So tell me adventurer, which spell will it be?")
     elif user_input == "heal" or user_input == "Heal":
         if player_spells[0] == "Heal":
             print("Peaty: Adventurer, you cant add Heal because you ALREADY HAVE HEAL! Please tell me you aren't an idiot and you're just testing me...on another thought don't tell me. Just tell me what level 2 spell you want to add.")
         elif player_spells[0] == "Pray":
             print("Peaty: Now, now, now, dont get greedy so early in the game adventurer. For you can only have ONE level 1 spell in your spellbook. Since you have already picked one, you must now pick a level 2 spell. So tell me adventurer, which spell will it be?")
     else:
         print("Peaty: I am sorry adventurer but I do not recognize that spell. Please choose a level 2 spell from my book.")
         
     
    
            
           
            
        