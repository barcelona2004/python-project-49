# !/usr/bin/env python3
import prompt

name = "MAX"


def hello():
    global name
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + "!")


def try_again():
    print(f"Let's try again, {name}!")


def win():
    print("Congratulations, " + name + "!")
