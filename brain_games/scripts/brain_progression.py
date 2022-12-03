from random import randint
import prompt

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print("What number is missing in the progression?")
    count = 0
    for _ in range(3):
        d = randint(1, 10)
        x = 0
        num = randint(3,8)
        k = 0
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
        line.strip()
        print(f'Question: {line}')
        answer = input()
        print(f"Your answer: {answer}")
        if int(lst[x]) + d == int(answer):
            print("Correct!")
            count += 1
        else:   
            print(f"{answer} is wrong answer ;(. Correct answer was {int(lst[x]) + d}.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")

