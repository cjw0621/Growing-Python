# This program will add guests to a room number, you can easily add and remove guests from the registry.
from random import randint


class GuestRegistration:
    if __name__ == "__main__":

        @staticmethod
        def name_registry():

            global tot_num_room
            print("Guest Registration Form tm.")
            print("Created by: Chase Whitney")
            print()
            input("Press Enter to start:")

            tot_num_room = 0
            guest_seat = {}
            empty_rooms = []
            count = 99
            master_user_info = {}
            recovery_question = []

            def tot_num_rooms_change():
                u_i = int(input("How many rooms do you have?\n"))
                tot_num_rooms_1 = int(u_i)
                global tot_num_room
                tot_num_room = tot_num_rooms_1
                print("**Successfully changed.**")
                return tot_num_room

            def make_pass_def(make_pass):
                count = 0
                symbol = ["!", "@", "#", "$", "%", "%", "^", "&", "&", "*"]
                for i in range(0, 10):
                    symbol.append(str(i))
                for i in symbol:
                    for k in make_pass:
                        if k in i:
                            count += 1
                if count >= 3:
                    master_user_info["password"] = str(make_pass)
                    count = 0
                    symbol.clear()
                else:
                    print("Password not strong enough.\nYou must add at least 3 numbers and symbols")
                    make_pass_new = input("Create a system password:\n")
                    return make_pass_def(make_pass_new)

            if count == 99:
                make_pass1 = input("Create a system password:\n")
                make_pass_def(make_pass1)
                make_recovery1 = input("Whats the first recovery question:\n")
                recovery_question.insert(-1, make_recovery1)
                recovery_answer1 = input("Type the first recover question answer:\n")
                make_recovery2 = input("Whats your second recovery question:\n")
                recovery_question.insert(-1, make_recovery2)
                recovery_answer2 = input("Type the second recovery question answer:\n")
                make_recovery3 = input("Whats your third recovery question:\n")
                recovery_question.insert(-1, make_recovery3)
                recovery_answer3 = input("Type the third recovery question answer:\n")
                master_user_info["recovery answer 1"] = recovery_answer1
                master_user_info["recovery answer 2"] = recovery_answer2
                master_user_info["recovery answer 3"] = recovery_answer3

                try:
                    length = int(input("\nHow many rooms do you have?\n"))
                    tot_num_room = length
                except ValueError:
                    print("\nPlease enter a valid number.")

            try:
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
                            edit = input("\nWho do you want to edit?\n-> ").title()
                            if edit in guest_seat:
                                new_name = input("\nWho do you want to replace {0} with?\n-> ".format(edit)).title()
                                if new_name in guest_seat:
                                    temp_storage = []
                                    temp_storage.append(guest_seat[new_name])
                                    guest_seat[new_name] = guest_seat[edit]
                                    guest_seat[edit] = temp_storage[-1]
                                    temp_storage.clear()
                                    print("**Guest registry has been successfully updated**\n")
                                else:
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
                                    empty_rooms.insert(count, guest_seat[Del_name])
                                    del guest_seat[Del_name]
                                    print("\n**Guest successfully removed**\n")
                                    confirm = input("\nWould you like to remove another Guest?\nY or N -> ").title()
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
                        Type av to view number of available rooms
                        Type */CTR to change you max number of rooms\n """)

                    elif guests == "*/Ctr":
                        ran_num = randint(0, 2)
                        password = input("Please enter the systems password to change total room number.\n")
                        try:
                            if str(password) == master_user_info["password"]:
                                tot_num_rooms_change()
                            else:
                                print("Password is not correct. Would you like to use the password recover?")
                                p_w_r = input("Y or N -> ").title()
                                if p_w_r == "Y":
                                    print(recovery_question[ran_num])
                                    answer = input("")
                                    try:
                                        if answer == master_user_info["recovery answer 1"]:
                                            print("Your password is {}".format(master_user_info["password"]))
                                        elif answer == master_user_info["recovery answer 2"]:
                                            print("Your password is {}".format(master_user_info["password"]))
                                        elif answer == master_user_info["recovery answer 3"]:
                                            print("Your password is {}".format(master_user_info["password"]))
                                    except KeyError:
                                        print("Invalid answer. Try again.")
                        except KeyError:
                            print("Invalid entry")

                    elif guests == "Av":
                        print(f"\n{tot_num_room - len(guest_seat)} rooms are available.\n")

                    elif len(guest_seat) == tot_num_room:
                        print("\n**Guest was not added...**\n")
                        print("**You have no more rooms available\n")

                    else:
                        if len(empty_rooms) > 0:
                            print("\n!!New Guests will be booked in {} first!!\n".format(empty_rooms[-1]))
                            guest_seat["{}".format(guests)] = "{}".format(empty_rooms[-1])
                            print("**{} was successfully booked into {}**\n".format(guests, empty_rooms[-1]))
                            empty_rooms.remove(empty_rooms[-1])

                        else:
                            count += 1
                            guest_seat["{}".format(guests)] = "Room No. {}".format(count)
                            print("\n**{} was successfully booked into Room No. {}.**\n".format(guests, count))
            except ValueError:
                print("Length must be an integer")


GuestRegistration.name_registry()
