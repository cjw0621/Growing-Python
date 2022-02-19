# This program will add guests to a room number, you can easily add and remove guests from the registry.
from random import randint


class GuestRegistration:

    def __init__(self):
        self.guest_seat = {}
        self.empty_rooms = []
        self.count = 99
        self.master_user_info = {}
        self.recovery_question = []
        self.tot_num_room = 0

    def create_registration(self):

        print("Guest Registration Form tm.")
        print("Created by: Chase Whitney")
        print()
        input("Press Enter to start:")
        self.guest_register()

    def tot_num_rooms_change(self):
        u_i = int(input("Whats your max number of rooms?\n"))
        tot_num_rooms_1 = int(u_i)
        self.tot_num_room = tot_num_rooms_1
        return self.tot_num_room

    def make_pass_def(self, make_pass):

        count = 0
        symbol = ["!", "@", "#", "$", "%", "%", "^", "&", "&", "*"]
        for i in range(0, 10):
            symbol.append(str(i))
        for i in symbol:
            for k in make_pass:
                if k in i:
                    count += 1
        if count >= 3:
            self.master_user_info["password"] = str(make_pass)
            count = 0
            symbol.clear()
        else:
            print(
                "\n!!Password not strong enough!!.\nYou must add at least 3 numbers and symbols to your password.!!\n")
            make_pass_new = input("Create a system password:\n")
            return self.make_pass_def(make_pass_new)

    def guest_register(self):

        if self.count == 99:
            make_pass = input("Create a system password:\n")
            self.make_pass_def(make_pass)
            print("\nYou will need to create a password recovery:\n")
            make_recovery1 = input("Whats the first recovery question:\n")
            self.recovery_question.insert(-1, make_recovery1)
            recovery_answer1 = input("Type the first recover question answer:\n")
            make_recovery2 = input("Whats your second recovery question:\n")
            self.recovery_question.insert(-1, make_recovery2)
            recovery_answer2 = input("Type the second recovery question answer:\n")
            make_recovery3 = input("Whats your third recovery question:\n")
            self.recovery_question.insert(-1, make_recovery3)
            recovery_answer3 = input("Type the third recovery question answer:\n")
            self.master_user_info["recovery answer 1"] = recovery_answer1
            self.master_user_info["recovery answer 2"] = recovery_answer2
            self.master_user_info["recovery answer 3"] = recovery_answer3

            try:
                length = int(input("\nWhats the your max number of rooms?\n"))
                self.tot_num_room = length
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
                    if len(self.guest_seat) == 0:
                        print("\n**You have no Guests in the Registry.**\n")
                    else:
                        for k, v in self.guest_seat.items():
                            print(k, ":", v)
                        edit = input("\nWho do you want to edit?\n-> ").title()
                        if edit in self.guest_seat:
                            new_name = input("\nWho do you want to replace {0} with?\n-> ".format(edit)).title()
                            if new_name in self.guest_seat:
                                temp_storage = []
                                temp_storage.append(self.guest_seat[new_name])
                                self.guest_seat[new_name] = self.guest_seat[edit]
                                self.guest_seat[edit] = temp_storage[-1]
                                temp_storage.clear()
                                print("**Guest registry has been successfully updated**\n")
                            else:
                                self.guest_seat[new_name] = self.guest_seat[edit]
                                del self.guest_seat[edit]
                                print("**Guest registry has been successfully updated**\n")
                        else:
                            print("**Guest is not found. Check the spelling and try again*\n")

                elif guests == "View":
                    if len(self.guest_seat) == 0:
                        print("\n**You have no Guests in the Registry.**\n**Please add a Guest**\n")
                    else:
                        print("Guest Registry: \n")
                        for k, v in self.guest_seat.items():
                            print(k, ":", v)

                elif self.guest_seat.get(guests):
                    print("\n**Guest is already in Registry**")
                    print("**" + self.guest_seat[guests] + "**\n")

                elif guests == "Del":
                    if len(self.guest_seat) == 0:
                        print("\n**You have no Guests in the Registry.**\n")
                    else:
                        print("Which guest would you like to remove from the Registry?\n")
                        for k, v in self.guest_seat.items():
                            print(k, ":", v)
                        while True:
                            if len(self.guest_seat) == 0:
                                print("\n**You have no more Guests in the Registry**\n")
                                break

                            del_name = input("\nEnter a name to delete\n-> ").title()
                            if self.guest_seat.get(del_name):
                                self.empty_rooms.insert(self.count,
                                                        self.guest_seat[del_name])
                                del self.guest_seat[del_name]
                                print("\n**Guest successfully removed**\n")
                                confirm = input("\nWould you like to remove another Guest?\nY or N -> ").title()
                                if confirm == "N":
                                    break
                                elif confirm == "Y":
                                    for k, v in self.guest_seat.items():
                                        print(k, ":", v)
                            else:
                                print("**Guests name does not exist in Registry. Check the name and try again.**")

                elif guests == "Help":
                    print("""
                            Type / to exit the program
                            Type Edit to edit your Guest Registry
                            Type a Guests name to add them to your Registry
                            Type View to view the Guests Registry
                            Type Del to remove Guest/s from the Registry
                            Type Av to view number of available rooms
                            Type */Ctr to change your max number of rooms available\n """)

                elif guests == "*/Ctr":
                    ran_num = randint(0, 2)
                    password = input(
                        "Please enter the systems password to change your maximum number of rooms.\n-> ")
                    try:
                        if str(password) == self.master_user_info["password"]:
                            self.tot_num_rooms_change()
                        else:
                            print("Password is not correct. Would you like to use the password recover?")
                            p_w_r = input("Y or N -> ").title()
                            while True:
                                if p_w_r == "Y":
                                    print(self.recovery_question[ran_num])
                                    answer = input("")
                                    try:
                                        if answer == self.master_user_info["recovery answer 1"]:
                                            print("Your password is {}".format(
                                                self.master_user_info["password"]))
                                            break
                                        elif answer == self.master_user_info["recovery answer 2"]:
                                            print("Your password is {}".format(
                                                self.master_user_info["password"]))
                                            break
                                        elif answer == self.master_user_info["recovery answer 3"]:
                                            print("Your password is {}".format(
                                                self.master_user_info["password"]))
                                            break

                                        else:
                                            print("Your answer did not match.\nWould you like to try again?")
                                            answer1 = input("").title()
                                            if answer1 == "Y":
                                                pass
                                            elif answer1 == "N":
                                                break
                                            else:
                                                print("Your response is unrecognized")
                                                break

                                    except KeyError:
                                        print("Invalid answer. Try again.")
                                elif p_w_r == "N":
                                    break
                                else:
                                    p_w_r = input("Please type either Y for yes or N for no.")

                    except KeyError:
                        print("Invalid entry")

                elif guests == "Av":
                    print(
                        f"\n{self.tot_num_room - len(self.guest_seat)} rooms are available.\n")

                elif len(self.guest_seat) == self.tot_num_room:
                    print("\n**Guest was not added...**\n")
                    print("**You have no more rooms available\n")

                else:
                    if len(self.empty_rooms) > 0:
                        print("\n!!New Guests will be booked in {} first!!\n".format(
                            self.empty_rooms[-1]))
                        self.guest_seat["{}".format(guests)] = "{}".format(
                            self.empty_rooms[-1])
                        print("**{} was successfully booked into {}**\n".format(guests,
                                                                                self.empty_rooms[-1]))
                        self.empty_rooms.remove(self.empty_rooms[-1])

                    else:
                        self.count += 1
                        self.guest_seat["{}".format(guests)] = "Room No. {}".format(
                            self.count)
                        print("\n**{} was successfully booked into Room No. {}.**\n".format(guests,
                                                                                            self.count))
        except ValueError:
            print("System Error")


if __name__ == "__main__":
    start = GuestRegistration()
    start.create_registration()
