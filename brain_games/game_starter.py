import prompt


def start_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")
    print(game.RULE)
    for _ in range(3):
        question, result = game.get_game()
        print(question)
        answer = prompt.string('Your answer: ')
        if str(answer) == str(result):
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer;(. "
                  f"Correct answer was '{result}'")
            print("Let's try again, " + name + "!")
            return
    print("Congratulations, " + name + "!")
