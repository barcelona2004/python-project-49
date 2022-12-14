from random import randint


def build_progression(d, num):
    x, k = 0, 0
    lst = []
    for i in range(1, d * 10 + 1, d):
        if k == num:
            lst.append('..')
            x = k - 1
            result = i
        else:
            lst.append(str(i))
        k += 1
    line = ""
    for j in lst:
        line += j
        line += ' '
    return line, lst, x, result


def get_game_progression():
    d = randint(1, 10)
    num = randint(1, 10)
    line, lst, x, result = build_progression(d, num)
    line = f"Question: {line}"
    return line, result
