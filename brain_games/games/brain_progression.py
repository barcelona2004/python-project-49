from random import randint


def create_progression(step, num):
    count, result = 0, 0
    lst = []
    for elem in range(1, step * 10 + 1, step):
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
    step = randint(1, 10)
    num = randint(1, 10)
    line, lst, result = create_progression(step, num)
    question = f"Question: {line}"
    return question, result
