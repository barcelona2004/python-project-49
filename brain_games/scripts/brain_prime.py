from brain_games.game_starter import hello, try_again, win
from brain_games.games.brain_prime import get_game_prime


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
        line, result = get_game_prime()
        print(line)
        answer = input()
        print(f"Your answer: {answer}")
        if answer != 'yes' and answer != 'no':
            try_again()
            return 0
        else:
            is_correct_answer(answer, result)
        count += 1
    if count == 3:
        win()


if __name__ == "__main__":
    main()
