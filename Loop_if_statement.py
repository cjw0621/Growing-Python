from random import randint

users_inv = set()

class Weapons:
    broad_sword = randint(1,5)
    short_sword = randint(1, 5)
    weapons = {
        "Broadsword": broad_sword,
        "Shortsword": short_sword
    }

def main1():
    while True:
        user_input = input("What would you like to start with?\nBroadsword or Shortsword?\n")
                 
        if user_input == "Broadsword" or user_input == "broadsword":
            users_inv.add("Broadsword")
            print("You curently have in your inventory:")
            for element in users_inv:
                print(element)
            user_input = input("Push enter to continue\n")
            return
            
        elif user_input == "Shortsword" or user_input == "shortsword":
            users_inv.add("Shortsword")
            print("You currently have in your inventory:")
            for element in users_inv:
                print(element)
            user_input = input("Push enter to continue\n")
            return
        
        else:
            print("\nI am sorry adventurer but I did not understand what you said.\n")
            
if __name__ == "__main__":
    main1()
