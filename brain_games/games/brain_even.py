from random import randint


def is_even(number):
    return number % 2 == 0


def main():
    random_number = randint(1, 1000)
    if is_even(random_number):
        result = 'yes'
    else:
        result = 'no'
    return random_number, result
