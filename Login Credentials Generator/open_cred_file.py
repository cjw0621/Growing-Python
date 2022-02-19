import os
import user_document_folder as udl
import encrypt_cred_file as ecf


def view_cred_file() -> None:
    # Checks the path for the login_credential.txt
    if os.path.exists(udl.DOC_LOC +
                          r'\Login Credentials\Login_Credential_Gen\database'
                          r'\key\login_credentials.txt'):
        # Checks the key file for `key.key`
        if os.path.exists(udl.DOC_LOC +
                          r'\Login Credentials\Login_Credential_Gen\database'
                          r'\key\key.key'):
            # Loads the encryption and decryption function to decrypt login cred
            key = ecf.load_key()
            ecf.decrypt(udl.DOC_LOC +
                        r'\Login Credentials\Login_Credential_Gen'
                        r'\database\key\login_credentials.txt', key)

            # Opens users cred file and prints data from the file
            with open(os.path.join(udl.DOC_LOC +
                                   r'\Login Credentials\Login_Credential_Gen'
                                   r'\database\key\login_credentials.txt'),
                                   "r") as f:
                line = f.readline()
                while line:
                    print(line, end="")
                    line = f.readline()

        else:
            # Writes encryption key `key.key` if not found in key folder
            ecf.write_key()
            key = ecf.load_key()
            ecf.encrypt(udl.DOC_LOC +
                        r'\Login Credentials\Login_Credential_Gen'
                        r'\database\key\login_credentials.txt', key)

            view_cred_file()
    else:
        # Prints 404 error if there isn't login_credential file.
        print("!"*70)
        print("                       Error: 404")
        print("                    File not found:\n        "
              "Your file was either "
              "deleted, corrupted,\nor moved. Please ensure the file is "
              "in the proper directory.")
        print("!"*70)

