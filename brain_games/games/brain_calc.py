from brain_games.games.brain_games import hello, try_again, win
from random import randint


def main():
    hello()
    print("What is the result of the expression?")
    first_sum = randint(1, 100)
    second_sum = randint(1, 100)
    first_dif = randint(1, 100)
    second_dif = randint(1, 100)
    first_tim = randint(1, 100)
    second_tim = randint(1, 100)
    print(f"Question: {first_sum} + {second_sum}")
    summary = input()
    print(f"Your answer: {summary}")
    if first_sum + second_sum == int(summary):
        print("Correct!")
        print(f"Question: {first_dif} - {second_dif}")
        differ = input()
        print(f"Your answer: {differ}")
        if first_dif - second_dif == int(differ):

            print("Correct!")
            print(f"Question: {first_tim} * {second_tim}")
            time = input()
            print(f"Your answer: {time}")
            if first_tim * second_tim == int(time):
                print("Correct!")
                win()
            else:
                print(f"'{time}' is wrong answer ;(."
                      f"Correct answer was '{first_tim * second_tim}'.")
                try_again()
        else:
            print(f"'{differ}' is wrong answer ;(."
                  f"Correct answer was '{first_dif - second_dif}'.")
            try_again()
    else:
        print(f"'{summary}' is wrong answer ;(."
              f"Correct answer was '{second_sum + first_sum}'.")
        try_again()


if __name__ == '__main__':
    main()
