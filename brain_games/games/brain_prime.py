from random import randint


def is_prime(number):
    for i in range(2, round(number ** 0.5) + 1):
        if number % i == 0:
            return 'no'
    return 'yes'


def get_game_prime():
    random_num = randint(1, 1000)
    result = is_prime(random_num)
    question = f"Question: {random_num}"
    return question, result
