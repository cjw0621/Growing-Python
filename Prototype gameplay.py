u_i =input("Whats your name?\n")

character = {}

character['Name'] = u_i

u_i = input("Whats your class?\nYou may choose either Paladin, Knight, Sorcerer\n")
if u_i == "paladin" or u_i == "Paladin":
    character['Class'] = "Paladin"
elif u_i == "Knight" or u_i == "knight":
    character['Class'] = "Knight"
elif u_i == "Sorcerer" or u_i == "sorcerer":
    character['Class'] = 'Sorcerer'
print("Your character profile:")    
for k, v in character.items(): # iterating through the dictionary, .items() is a must have for syntax to be valid
    print(k, ':', v)

print(f"Congratulations {character['Name']}, you have aquired 6 gc for completing this quest")
character['gc'] = 0
character['gc'] = character['gc'] + 6
print('You now have:')
print(character['gc'],"gold coins in your coin bag.")    

def Get_char_info(u_i):
    if u_i == "coin bag" or u_i == "Coin bag":
        print(f"Your coin bag contains {character['gc']} gold coins")
    elif u_i == "Level" or u_i == "level":
        print(f"Your current level is {character['Level']}")
def Call_info():
        u_i = input('What would you like to view?\n')
        Get_char_info(u_i)
        
character['Level'] = 1

u_i =input()

if u_i == "info" or u_i == "Info":
    u_i = input("What would you like to view?\nSystem: You may view your current level or you may view your coin bag\nType here -> ")
    Get_char_info(u_i)

def Level_1_quest():
    print('kill the knight')
    u_i = input("Do you want to attack the knight?\n")
    if u_i == 'yes':
        print("You attacked the knight and now hes dead")
        u_i = input("Do you wish to continue?\n")
        if u_i == 'yes':
            Level_2_quest()
            
def Level_2_quest():
    print("congrats on making it to level 2!\nYou have gained experience from comoleting level 1!")    
    character['Level'] = 2
    print(f"You are now level {character['Level']}!")
    u_i = input('What would you like to do now?\n')
    if u_i == "info" or u_i == "Info":
        Call_info()
    
    
        
            
                
                    
                        
                                
u_i = input("Lets get on with the adventure shall we?\nHeres the story:\nA black knight has wrecked havoc in our small town, he is currently residing in the pub\nDo you accept?")    

if u_i == "yes":
    Level_1_quest()