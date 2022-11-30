from random import randint
import prompt


def main():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    for i in range(3):  
        random_number = randint(1, 100)
        print("Question: " + str(random_number))
        x = input()
        print("Your answer: " + x)
        if x != 'yes' and x != 'no':
            print("Let's try again, " + name + "!")
            break
        else:
            if random_number % 2 == 0 and x == 'yes':
                print("Correct!")
            elif random_number % 2 != 0 and x == 'no':
                print("Correct!")
            elif random_number % 2 == 0 and x == 'no':
                print("'no' is wrong answer ;(. Correct answer was 'yes'.")
                print("Let's try again, " + name + "!")
                break
            else:
                print("'yes' is wrong answer ;(. Correct answer was 'no'.")
                print("Let's try again, " + name + "!")
                break
        count += 1
    if count == 3:
        print("Congratulations, " + name + "!")

            
if __name__ == '__main__':
    main()

