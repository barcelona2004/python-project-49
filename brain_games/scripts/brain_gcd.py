from random import randint
import prompt

def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print("Find the greatest common divisor of given numbers.")
    count = 0
    for i in range(3):
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        print(f"Question: {number1} {number2}")
        answer = input()
        print(f"Your answer: {answer}")
        max_num = 0
        for i in range(1, min(number1,number2)+1):
            if number2 % i == 0 and number1 % i == 0:
                max_num = max(max_num, i)
        if max_num == int(answer):
            print("Correct!")
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{max_num}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f"Congratulations, {name}!")

