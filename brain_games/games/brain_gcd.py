from random import randint


def is_gcd(number1, number2):
    max_num = 0
    for i in range(1, min(number1, number2) + 1):
        if number2 % i == 0 and number1 % i == 0:
            max_num = max(max_num, i)
    return max_num


def main():
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    if is_gcd(random_number1, random_number2):
        result = 'yes'
    else:
        result = 'no'
    return result
