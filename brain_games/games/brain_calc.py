from random import randint, choice


OPERATORS = ['+', '-', '*']


def calculate(num1, num2, operator):
    if operator == '*':
        return num1 * num2
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2


def get_game_calc():
    variants = 'What is the result of the expression?'
    random_operator = choice(OPERATORS)
    random_num1 = randint(1, 100)
    random_num2 = randint(1, 100)
    question = f"Question: {random_num1} {random_operator} {random_num2}"
    result = calculate(random_num1, random_num2, random_operator)
    return question, result, variants
