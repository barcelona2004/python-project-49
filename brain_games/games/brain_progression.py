from random import randint


def build_progression(d, num):
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


def get_game_progression():
    d = randint(1, 10)
    num = randint(1, 10)
    line, lst, x = build_progression(d, num)
    result = int(lst[x]) + d
    line = f"Question: {line}"
    return line, result
