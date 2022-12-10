from brain_games.games.brain_games import hello, try_again, win
from random import randint


def gcd(number1, number2):
    max_num = 0
    for i in range(1, min(number1, number2) + 1):
        if number2 % i == 0 and number1 % i == 0:
            max_num = max(max_num, i)
    return max_num


def main():
    hello()
    print("Find the greatest common divisor of given numbers.")
    count = 0
    for i in range(3):
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        print(f"Question: {number1} {number2}")
        answer = input()
        print(f"Your answer: {answer}")
        max_num = gcd(number1, number2)
        if max_num == int(answer):
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{max_num}'.")
            try_again()
            break
    if count == 3:
        win()


if __name__ == "__main__":
    main()
