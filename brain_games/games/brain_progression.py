from brain_games.games.brain_games import hello, try_again, win
from random import randint


def main():
    hello()
    print("What number is missing in the progression?")
    count = 0
    for _ in range(3):
        d = randint(1, 10)
        num = randint(3, 8)
        line, lst, x = nums(d, num)
        print(f'Question: {line}')
        answer = input()
        print(f"Your answer: {answer}")
        if int(lst[x]) + d == int(answer):
            print("Correct!")
            count += 1
        else:
            print(f"{answer} is wrong answer ;(."
                  f"Correct answer was {int(lst[x]) + d}.")
            try_again()
            break
    if count == 3:
        win()


def nums(d, num):
    x, k = 0, 0
    lst = []
    for i in range(1, d * 10 + 1, d):
        if k == num:
            lst.append('..')
            x = k - 1
        else:
            lst.append(str(i))
        k += 1
    line = ""
    for j in lst:
        line += j
        line += ' '
    return line, lst, x


if __name__ == "__main__":
    main()
