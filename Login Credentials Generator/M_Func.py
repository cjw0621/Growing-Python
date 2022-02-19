import password_generator as pg
import user_login as ul
import user_document_folder as udl
import encrypt_cred_file as ecf
import time
import os
from os import path


class UserCred:

    def __init__(self):
        self.USER_PATH = udl.DOC_LOC
        self.star = "*" * 50
        self.line = "-" * 50

        # Checks the User's Document's folder for the 'Login Credential'
        # folder
        self.FILE = (udl.DOC_LOC +
                     r"\Login Credentials\Login_Credential_Gen"
                     r"\database\key\login_credentials.txt")
        self.KEY_LOC = (udl.DOC_LOC +
                        r"\Login Credentials\Login_Credential_Gen"
                        r"\database\key\key.key")

    def cred_file(self) -> None:
        """
        Generates a .txt file that stores the users generated username and
        password. Also displays the users randomly generated username and
        password.
        """
        username = ul.UsernameGen().gen_user_name()
        time.sleep(1)
        password = pg.GenPass().gen_password()
        time.sleep(1)
        print()
        print("Your username is:")
        print("*" * len(username))
        print(username)
        print("*" * len(username))
        print()
        print("Your password is:")
        print("*" * len(username))
        print(password)
        print("*" * len(username))
        time.sleep(1)
        print()
        user_input = input("Would you like to save your login "
                           "credentials?\n=> ").casefold()
        if user_input == "yes" or user_input == "y":
            # Opens the existing file
            if os.path.exists(self.FILE):
                print("Opening 'login_credentials' file...")
                key = ecf.load_key()
                ecf.decrypt(self.FILE, key)
                time.sleep(1)
                print("File successfully opened.")
                time.sleep(1)
                print()
                user_input = input("What application are the "
                                   "credentials for?\n=> ").upper()
                while True:
                    with open(os.path.join(self.FILE), "r") as f:
                        application = f.read()
                        if user_input in application.split():
                            print("This application name already has a "
                                  "login credential.\nPlease modify the "
                                  "name.")
                            time.sleep(1)
                            user_input = input("What application are the "
                                               "credentials for?\n=> ").upper()
                        else:
                            with open(os.path.join(self.FILE), "a") as f:

                                f.write(self.star + "\n")
                                f.write(user_input + "\n")
                                f.write(self.line + "\n")
                                f.write("Username: " + username + "\n")
                                f.write("Password: " + password + "\n")
                                f.write(self.star + "\n")
                                f.write("\n")
                                f.close()

                                print("Saving File...")
                                time.sleep(1)
                                saved = "Your login credentials has been " \
                                        "saved into your Document's folder"
                                print("*" * len(saved))
                                print(saved)
                                print("*" * len(saved))
                                if os.path.exists(self.USER_PATH +
                                  r'\Login Credentials\Login_Credential_Gen '
                                  r'\database\key\key.key'):

                                    key = ecf.load_key()
                                    ecf.encrypt(self.FILE, key)
                                    break
                                else:
                                    ecf.write_key()
                                    key = ecf.load_key()
                                    ecf.encrypt(self.FILE, key)
                                    break
            else:
                print("Creating new login credential file...")
                time.sleep(1)

                """
                Creates a directory called 'Login Credentials' in the users 
                document folder.
                """

                # Directory name
                directory = r'Login Credentials\Login_Credential_Gen\database\key'
                # Parent Directory path to users default Document folder
                # location
                parent_dir = self.USER_PATH
                # Path
                dir_path = os.path.join(parent_dir, directory)
                # Create the directory
                # 'Login Credential' in users Document folder
                os.mkdir(dir_path)
                print("Login credential file created.")
                time.sleep(1)

                """
                Creates a new file that stores users login credentials.
                """

                user_input = input("What service are the credentials for?"
                                   "\n=> ").upper()

                with open(os.path.join(self.FILE), "w") as f:
                    f.write(self.star + "\n")
                    f.write(user_input + "\n")
                    f.write(self.line + "\n")
                    f.write("Username: " + username + "\n")
                    f.write("Password: " + password + "\n")
                    f.write(self.star + "\n")
                    f.write("\n")
                    f.close()

                    print("Saving File...")
                    time.sleep(1)
                    saved = "Your login credentials has been " \
                            "saved into your Document's folder"
                    print("*" * len(saved))
                    print(saved)
                    print("*" * len(saved))

                    if os.path.exists(self.USER_PATH +
                                      r'\Login Credentials\Login_Credential_Gen '
                                      r'\database\key\key.key'):
                        key = ecf.load_key()
                        ecf.encrypt(self.FILE, key)

                    else:
                        ecf.write_key()
                        key = ecf.load_key()
                        ecf.encrypt(self.FILE, key)

        elif user_input == "no" or user_input == "n":
            print("Login credentials was not saved.")
            print()
            time.sleep(1)
        else:
            print()
            print("*" * 30)
            print("Please type 'yes' or 'no'")
            print("*" * 30)
            time.sleep(1)
            print()

    def gen_pas(self) -> None:

        """
        saves the randomly generated password to a .txt file in the users
        Documents folder. The user generates their own username and saves the
        users username and a randomly generated password into a .txt file.
        """
        while True:

            if path.exists(self.FILE):
                password = pg.GenPass().gen_password()
                time.sleep(1)
                print("Your password is:")
                print("*" * len(password))
                print(password)
                print("*" * len(password))
                time.sleep(1)
                user_input = input("Would you like to save your login "
                                   "credentials?\n=>").casefold()
                if user_input == "yes" or user_input == "y":
                    print()
                    print("Decrypting file...")
                    # Checks path for existing key.key file
                    if os.path.exists(self.KEY_LOC):
                        key = ecf.load_key()
                        ecf.decrypt(self.FILE, key)

                    # Creates key.key file
                    else:
                        ecf.write_key()

                    time.sleep(1)
                    print("File successfully unencrypted.")
                    print()
                    user_app_name = input("Enter application name\n=> ").upper()

                    while True:

                        with open(os.path.join(self.FILE), "r") as f:
                            application = f.read()
                            if user_app_name in application.split():
                                print("This application name already has a "
                                      "login credential.\nPlease modify the "
                                      "name.")
                                time.sleep(1)
                                user_app_name = input(
                                    "What application are the credentials for?"
                                    "\n=> ").upper()

                        user_username = input("Enter in your username\n=> ")
                        print("Saving login information...")
                        time.sleep(1)
                        # Appends the users self generated username and
                        # randomly generated password
                        with open(self.FILE, 'a') as f:
                            f.write(self.star + "\n")
                            f.write(user_app_name + "\n")
                            f.write(self.line + "\n")
                            f.write("Username: " + user_username + "\n")
                            f.write("Password: " + password + "\n")
                            f.write(self.star + "\n")
                            f.write("\n")
                            f.close()
                            key = ecf.load_key()
                            ecf.encrypt(self.FILE, key)
                        time.sleep(1)
                        saved = "Your login credentials has been saved into " \
                                "your Document's folder"
                        print("*" * len(saved))
                        print(saved)
                        print("*" * len(saved))
                        break
                    break

                elif user_input == "no" or user_input == "n":
                    time.sleep(1)
                    print("Login credentials were not saved")
                    break
            else:
                """
                Creates a directory called 'Login Credentials' in the users 
                document folder.
                """

                # Directory name
                directory = r"Login Credentials\Login_Credential_Gen"
                r"\database\key"
                # Parent Directory path to users default Document folder
                # location
                parent_dir = self.USER_PATH
                # Path
                dir_path = os.path.join(parent_dir, directory)
                # Create the directory
                # 'Login Credential' in users Document folder
                os.mkdir(dir_path)

                with open(os.path.join(self.FILE), "a") as f:
                    f.write('')
                print("Login credential file created.")
                if os.path.exists(self.KEY_LOC):
                    key = ecf.load_key()
                    ecf.encrypt(self.FILE, key)

                    # Creates key.key file
                else:
                    ecf.write_key()
                    key = ecf.load_key()
                    ecf.encrypt(self.FILE, key)
                time.sleep(1)


if __name__ == "__main__":
    UserCred().cred_file()
    UserCred().gen_pas()
