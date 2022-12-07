from brain_games.games.brain_games import hello, try_again, win
from random import randint


def main():
    hello()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    for i in range(3):
        random_number = randint(1, 100)
        print("Question: " + str(random_number))
        x = input()
        print("Your answer: " + x)
        if x != 'yes' and x != 'no':
            try_again()
            break
        else:
            if (random_number % 2 == 0 and x == 'yes') or \
                    (random_number % 2 != 0 and x == 'no'):
                print("Correct!")
            elif random_number % 2 == 0 and x == 'no':
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                try_again()
                break
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                try_again()
                break
        count += 1
    if count == 3:
        win()


if __name__ == '__main__':
    main()
