import prompt


def starter(function):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    question_none, result_none, variants = function()
    print(variants)
    count = 0
    for _ in range(3):
        question, result, variants_none = function()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer;(. "
                  f"Correct answer was '{result}'")
            print("Let's try again, " + name + "!")
            exit(0)
    if count == 3:
        print("Congratulations, " + name + "!")
