from random import randint


RULE = 'What number is missing in the progression?'


def get_progression_result(step, num):
    count, result = 0, 0
    start = randint(1, 100)
    lst = []
    for elem in range(start, start + step * 10 + 1, step):
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


def get_game():
    step = randint(1, 10)
    num = randint(1, 10)
    line, lst, result = get_progression_result(step, num)
    question = f"Question: {line}"
    return question, result
