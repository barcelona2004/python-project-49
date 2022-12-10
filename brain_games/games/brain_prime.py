from brain_games.games.brain_games import hello, try_again, win
from random import randint


def is_prime(number):
    for i in range(2, round(number ** 0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def is_correct_answer(answer, correct_answer):
    if correct_answer == answer:
        print("Correct!")
    else:
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{correct_answer}'.")
        try_again()
        exit(0)


def main():
    hello()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    for _ in range(3):
        random_number = randint(1, 1000)
        correct_answer = is_prime(random_number)
        print(f"Question: {random_number}")
        answer = input()
        print(f"Your answer: {answer}")
        if answer != 'yes' and answer != 'no':
            try_again()
            return 0
        else:
            is_correct_answer(answer, correct_answer)
        count += 1
    if count == 3:
        win()


if __name__ == "__main__":
    main()
