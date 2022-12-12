from random import randint 


def nums(d, num):
    x, k = 0, 0
    lst = []
    for i in range(1, d * 10 + 1, d):
        if k == num:
            lst.append('..')
            x = k - 1
        else:
            lst.append(str(i))
            k += 1
            line = ""
    for j in lst:
        line += j
        line += ' '
    return line, lst, x


def main():
    d = randint(1, 10)
    num = randint(1, 10)
    line, lst, x = nums(d, num)
    if lst[x] + d:
        return 'yes'
    else:
        return 'no'
