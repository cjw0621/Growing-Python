import os.path

import M_Func
import time
import encrypt_cred_file as ecf
import user_document_folder as udl
import open_cred_file

print("*" * 50)
print("Welcome to Username and Password generator.")
print("*" * 50)
time.sleep(2)
print()
while True:
    user_input = input("Type 1 if you want to generate a username and a "
                       "password.\nType 2 if you want to just generate a "
                       "password.\nType 3 to view your credentials.\nType 0 to "
                       "close the "
                       "window.\n=> ").casefold()

    if user_input == "1":
        #   Runs the main function that creates usernames and passwords.
        M_Func.UserCred().cred_file()

    elif user_input == "2":
        M_Func.UserCred().gen_pas()

    elif user_input == "3":
        print("Opening user credentials...")
        print()
        time.sleep(1)
        open_cred_file.view_cred_file()
        time.sleep(1)
        key = ecf.load_key()
        ecf.encrypt(udl.DOC_LOC +
                    r'\Login Credentials\Login_Credential_Gen'
                    r'\database\key\login_credentials.txt', key)

    elif user_input == "0":
        print("Closing the window...")
        key = ecf.load_key()
        if os.path.exists(udl.DOC_LOC +
                          r'\Login Credentials\Login_Credential_Gen'
                          r'\database\key\key.key'):
            time.sleep(1)
            break
        else:
            key = ecf.load_key()
            ecf.encrypt(udl.DOC_LOC +
                        r'\Login Credentials\Login_Credential_Gen'
                        r'\database\key\login_credentials.txt', key)

            time.sleep(2)
            break

    else:
        print()
        print("*" * 18)
        print("Invalid response")
        print("*" * 18)
        print()
