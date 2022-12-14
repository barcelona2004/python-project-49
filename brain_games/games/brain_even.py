from random import randint


def is_even(num):
    return num % 2 == 0


def get_game_even():
    random_num = randint(1, 1000)
    line = f"Question: {random_num}"
    if is_even(random_num):
        result = 'yes'
    else:
        result = 'no'
    return line, result, random_num
