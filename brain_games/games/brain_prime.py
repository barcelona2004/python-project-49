from random import randint


def is_prime(number):
    return number > 1 and \
        all(number % i != 0 for i in range(2, round(number ** 0.5) + 1))


def main():
    random_number = randint(1, 1000)
    if is_prime(random_number):
        result = 'yes'
    else:
        result = 'no'
    return result
