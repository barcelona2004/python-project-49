from random import randint


def is_right_sum(number1, number2):
    return number1 + number2


def is_right_dif(number1, number2, diff):
    return number1 - number2 == diff


def is_right_times(number1, number2, time):
    return number1 * number2 == time


def main():
    random_summ1 = randint(1, 100)
    random_summ2 = randint(1, 100)
    random_diff1 = randint(1, 100)
    random_diff2 = randint(1, 100)
    random_tim1 = randint(1, 100)
    random_tim2 = randint(1, 100)
    if is_right_summ(random_summ1, random_summ2):
        result_summ = 'yes'
    if is_right_diff(random_diff1, random_diff2):
        result_diff = 'yes'
    if is_right_time(random_tim1, random_tim2):
        result_time = 'yes'
    return result_summ, result_diff, result_time
