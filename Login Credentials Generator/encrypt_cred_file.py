import os
import user_document_folder as udl
from cryptography.fernet import Fernet


def write_key() -> None:
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open(udl.DOC_LOC + r"\Login "
                            r"Credentials\Login_Credential_Gen\database"
                            r"\key\key.key",
              'wb') as key_file:
        key_file.write(key)


def load_key() -> bytes:
    """
    Loads the key from the current directory named `key.key`
    :return: The encryption key from `key.key`
    """
    return open(udl.DOC_LOC + r"\Login "
                              r"Credentials\Login_Credential_Gen\database\key"
                              r"\key.key", 'rb').read()


def encrypt(filename: str, key: bytes) -> None:
    """
    Given a file name `str` and key `bytes`, it encrypts the file and write it
    :param filename:    Directory and name of file to encrypt
    :param key:     Encryption key
    """
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # read all file data
        file_data = file.read()

    # encrypt data
    encrypted_data = f.encrypt(file_data)

    # write the encrypted file
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename: str, key: bytes) -> None:
    """
    Give a filename `Str` and key `bytes`, it decrypts the file and write it
    :param filename:    Name of file to encrypt
    :param key:     Encryption key
    """

    f = Fernet(key)

    with open(filename, 'rb') as file:
        # read the encrypted data
        encrypted_data = file.read()

    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)

    # write the original file
    with open(filename, 'wb') as file:
        file.write(decrypted_data)
