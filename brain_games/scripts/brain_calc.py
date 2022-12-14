from brain_games.game_starter import hello, try_again, win
from brain_games.games.brain_calc import get_game_calc, calculate


def main():
    hello()
    print("What is the result of the expression?")
    count = 0
    for _ in range(3):
        line, result, operator, random_num1, random_num2 = get_game_calc()
        print(line)
        answer = input()
        print(f"Your answer: {answer}")
        correct_answer = calculate(random_num1, random_num2, operator)
        if correct_answer == int(answer):
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.")
            try_again()
            exit(0)
    if count == 3:
        win()


if __name__ == '__main__':
    main()
