from random import randint
import prompt


def is_prime(x):
    return x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    for _ in range(3):
        x = randint(1, 1000)
        print(f"Question: {x}")
        answer = input()
        print(f"Your answer: {answer}")
        if answer == 'yes' or answer == 'no':
            if is_prime(x) and answer == 'yes':
                print("Correct!")
            elif not is_prime(x) and answer == 'no':
                print("Correct!")
            elif is_prime(x) and answer == 'no':
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again {name}")
                break
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again {name}")
                break
        else:
            print(f"Let's try again {name}")
            break
        count += 1
    if count == 3:
        print(f"Congratulations, {name}!")
