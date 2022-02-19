import random
import time
from random import randint


class GenPass:

    def __init__(self):
        self.lower = 'abcdefghijklmnopqrstuvwxyz'
        self.upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.number = "0123456789"
        self.sym = '!@#$%&*,.;'
        self.ran_len = randint(15, 20)
        self.together = self.lower + self.upper + self.sym + self.number + \
                        self.number
        self.length = self.ran_len

    def gen_password(self):
        """
        Generates a random alphanumeric password for the user
        :return:  A randomly generated password
        """
        password = ''.join(random.sample(self.together, self.length))
        print("Generating password...")
        counter = 0
        for num in password:
            if num in self.number:
                counter += 1

        if counter < 2:
            time.sleep(2)
            return self.gen_password()
        else:
            time.sleep(2)
            print("Password created.")
            return password


if __name__ == "__main__":
    GenPass().gen_password()
