from brain_games.games.brain_games import hello, try_again, win
from random import randint


def is_prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


def main():
    hello()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    for _ in range(3):
        x = randint(1, 1000)
        print(f"Question: {x}")
        answer = input()
        print(f"Your answer: {answer}")
        if answer == 'yes' or answer == 'no':
            if (is_prime(x) and answer == 'yes') or \
                    (not is_prime(x) and answer == 'no'):
                print("Correct!")
            elif is_prime(x) and answer == 'no':
                print("'no' is wrong answer ;(."
                      "Correct answer was 'yes'.")
                try_again()
                break
            else:
                print("'yes' is wrong answer ;(."
                      "Correct answer was 'no'.")
                try_again()
                break
        else:
            try_again()
            break
        count += 1
    if count == 3:
        win()


if __name__ == "__main__":
    main()
