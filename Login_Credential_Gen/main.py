import M_Func
import time

print("*" * 50)
print("Welcome to Username and Password generator.")
print("*" * 50)
time.sleep(2)
print()
while True:
    user_input = input("Type 1 if you want to generate a username and a "
                       "password.\nType 2 if you want to just generate a "
                       "password.\nType 0 to close the window.\n=> ").casefold()

    if user_input == "1":
        #   Runs the main function that creates usernames and passwords.
        M_Func.UserCred().cred_file()

    elif user_input == "2":
        M_Func.UserCred().gen_pas()

    elif user_input == "0":
        print("Closing the window...")
        time.sleep(2)
        break

    else:
        print()
        print("*" * 18)
        print("Invalid response")
        print("*" * 18)
        print()
