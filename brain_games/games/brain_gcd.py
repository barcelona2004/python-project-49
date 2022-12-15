from random import randint


def max_gcd(num1, num2):
    max_num = 0
    for i in range(1, min(num1, num2) + 1):
        if num2 % i == 0 and num1 % i == 0:
            max_num = max(max_num, i)
    return max_num


def get_game_gcd():
    random_num1 = randint(1, 100)
    random_num2 = randint(1, 100)
    result = max_gcd(random_num1, random_num2)
    question = f"Question: {random_num1} {random_num2}"
    return question, result
