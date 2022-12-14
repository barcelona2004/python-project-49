from random import randint, choice


def calculate(num1, num2, operator):
    if operator == '*':
        return num1 * num2
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2


def get_game_calc():
    lst = ['+', '-', '*']
    random_operator = choice(lst)
    random_num1 = randint(1, 100)
    random_num2 = randint(1, 100)
    line = f"Question: {random_num1} {random_operator} {random_num2}"
    result = calculate(random_num1, random_num2, random_operator)
    return line, result, random_operator, random_num1, random_num2
