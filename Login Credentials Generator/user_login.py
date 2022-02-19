import english_words
from random import randint
import time


class UsernameGen:

    def __init__(self):
        self.word_set = english_words.english_words_alpha_set
        self.word_list = list(self.word_set)
        self.length = randint(2, 4)
        self.num_list = []

    def gen_user_name(self):
        """
        Randomly generates a username using words from the english_words dict.
        :return:    A randomly generated alphanumeric username.
        """
        pos_user_name = []
        for index in range(2):
            words = self.word_list[index]
            pos_user_name.append(words.title())
        for num in range(self.length):
            self.num_list.append(str(num))
        for self.ran_num in self.num_list:
            pos_user_name.append(str(randint(0, len(self.num_list))))
        username = ''.join(pos_user_name)
        print("Generating username...")
        time.sleep(2)
        print("Username created.")
        return username


if __name__ == "__main__":
    UsernameGen().gen_user_name()
