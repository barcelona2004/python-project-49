from brain_games.game_starter import hello, try_again, win
from brain_games.games.brain_gcd import get_game_gcd


def main():
    hello()
    print("Find the greatest common divisor of given numbers.")
    count = 0
    for _ in range(3):
        line, result = get_game_gcd()
        print(line)
        answer = input()
        print(f"Your answer: {answer}")
        if result == int(answer):
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{result}'.")
            try_again()
            exit(0)
    if count == 3:
        win()


if __name__ == "__main__":
    main()
