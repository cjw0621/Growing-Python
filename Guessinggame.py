from random import randint


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("Invalid number.")


highest = 1000

answer = randint(1, highest)

guess = 0
while guess != answer:
    print("Please guess a number between 1 - {}: ".format(highest))
    guess = get_integer(": ")

    if guess == 0:
        break

    if guess < answer:  # guess must be lower than answer
        print("Please answer higher")

    elif guess > answer:  # guess must be greater than answer
        print("Please guess lower")

    else:
        print("well done, you guessed it")
        print("Play again?")
        user_input = input(": ").lower()
        if user_input == "yes":
            answer = randint(1, highest)
            guess = ""
        else:
            print("Thanks for playing!")
            break

