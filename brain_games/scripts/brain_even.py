from brain_games.game_starter import hello, try_again, win
from brain_games.games.brain_even import get_game_even, is_even


def is_even_num(random_num, answer, correct_answer):
    if (is_even(random_num) and answer == 'yes') or \
            (not is_even(random_num) and answer == 'no'):
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
        line, result, random_num = get_game_even()
        print(line)
        answer = input()
        print("Your answer: " + answer)
        if answer != 'yes' and answer != 'no':
            try_again()
            return 0
        else:
            is_even_num(random_num, answer, result)
        count += 1
    if count == 3:
        win()


if __name__ == '__main__':
    main()
