from brain_games.games.brain_games import hello, try_again, win
from random import randint


def is_correct_answer(random_number):
    if random_number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def is_even(random_number, answer, correct_answer):
    if (random_number % 2 == 0 and answer == 'yes') or \
            (random_number % 2 != 0 and answer == 'no'):
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.")
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
        correct_answer = is_correct_answer(random_number)
        print("Your answer: " + answer)
        if answer != 'yes' and answer != 'no':
            try_again()
            return 0
        else:
            is_even(random_number, answer, correct_answer)
        count += 1
    if count == 3:
        win()


if __name__ == '__main__':
    main()
