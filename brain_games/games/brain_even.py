from brain_games.games.brain_games import hello, try_again, win
from random import randint


def is_even(random_number, answer):
    if (random_number % 2 == 0 and answer == 'yes') or \
            (random_number % 2 != 0 and answer == 'no'):
        print("Correct!")
    elif random_number % 2 == 0 and answer == 'no':
        print("'no' is wrong answer ;(. Correct answer was 'yes'.")
        try_again()
        exit(0)
    else:
        print("'yes' is wrong answer ;(. Correct answer was 'no'.")
        try_again()
        exit(0)


def main():
    hello()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    for i in range(3):
        random_number = randint(1, 100)
        print("Question: " + str(random_number))
        answer = input()
        print("Your answer: " + answer)
        if answer != 'yes' and answer != 'no':
            try_again()
            return 0
        else:
            is_even(random_number, answer)
        count += 1
    if count == 3:
        win()


if __name__ == '__main__':
    main()
