#This program will add guests to a room number, you can easly add and remove guests from the registry.
guest_seat = {}
count = 99
print("Guest Registration Form tm.")
print("Created by: Chase Whitney")
print()
input("Press Enter to start:")

while True:
    try:
        length = int(input("\nHow many rooms do you have?\n"))
        break
    except ValueError:
        print("\nPlease enter a valid number.")

while True:
    guests = input("\nEnter a Guests name or a command.\nType help to view available commands:\n-> ")
    guests = guests.title()
    if guests == "/":
        print("Program Exited")
        break

    elif guests == "Edit":
        if len(guest_seat) == 0:
            print("\n**You have no Guests in the Registry.**\n")
        else:
            for k, v in guest_seat.items():
                print(k, ":", v)
            edit = input("Who do you want to edit?\n-> ").title()
            if edit in guest_seat:
                new_name = input("Who do you want to replace {0} with?\n-> ".format(edit)).title()
                guest_seat[new_name] = guest_seat[edit]
                del guest_seat[edit]
                print("**Guest registry has been successfully updated**\n")
            else:
                print("**Guest is not found. Check the spelling and try again*\n")

    elif guests == "View":
        if len(guest_seat) == 0:
            print("\n**You have no Guests in the Registry.**\n**Please add a Guest**\n")
        else:
            print("Guest Registry: \n")
            for k, v in guest_seat.items():
                print(k, ":", v)

    elif guest_seat.get(guests):
        print("\n**Guest is already in Registry**")
        print("**" + guest_seat[guests] + "**\n")

    elif guests == "Del":
        if len(guest_seat) == 0:
            print("\n**You have no Guests in the Registry.**\n")
        else:
            print("Which guest would you like to remove from the Registry?\n")
            for k, v in guest_seat.items():
                print(k, ":", v)
            while True:
                if len(guest_seat) == 0:
                    print("\n**You have no more Guests in the Registry**\n")
                    break

                Del_name = input("\nEnter a name to delete\n-> ").title()
                if guest_seat.get(Del_name):
                    del guest_seat[Del_name]
                    print("\n**Guest successfully removed**\n")
                    count -= 1
                    confirm = input("\nWould you like to remove another Guest?\ny or n -> ").title()
                    if confirm == "N":
                        break
                    elif confirm == "Y":
                        for k, v in guest_seat.items():
                            print(k, ":", v)


                else:
                    print("**Guests name does not exist in Registry. Check the name and try again.**")

    elif guests == "Help":
        print("""
        Type / to exit the program
        Type edit to edit Guest Registry
        Type a Guests name to add them to Registry
        Type view to view the Guests Registry
        Type del to remove Guest/s from the Registry
        Type av to view number of available rooms\n """)

    elif guests == "Av":
        print(f"\n{length - len(guest_seat)} rooms are available.\n")

    elif len(guest_seat) >= length:
        print("\n**Guest was not added...**\n")
        print("**You have no more rooms available\n")

    else:
        count += 1
        guest_seat["{}".format(guests)] = "Room No. " + str(count)
        print(f"\n**{guests} was successfully added to registry.**\n")
