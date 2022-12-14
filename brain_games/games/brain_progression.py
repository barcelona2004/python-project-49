from random import randint


def build_progression(d, num):
    count, result = 0, 0
    lst = []
    for elem in range(1, d * 10 + 1, d):
        if count == num:
            lst.append('..')
            result = elem
        else:
            lst.append(str(elem))
        count += 1
    line = ""
    for elem in lst:
        line += elem
        line += ' '
    return line, lst, result


def get_game_progression():
    d = randint(1, 10)
    num = randint(1, 10)
    line, lst, result = build_progression(d, num)
    line = f"Question: {line}"
    return line, result
