from random import randint


def is_even(num):
    return num % 2 == 0


def get_game_even():
    variants = 'Answer "yes" if the number is even, otherwise answer "no".'
    random_num = randint(1, 1000)
    question = f"Question: {random_num}"
    if is_even(random_num):
        result = 'yes'
    else:
        result = 'no'
    return question, result, variants
