#!/usr/bin/env python
import random
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def new_question():
    random.seed()
    parity = random.randint(1, 99)
    return parity


def correct_answer(parity):
    if parity % 2 == 0:
        return 'yes'
    else:
        return 'no'


def parity_check_game():
    player_name = welcome_user()
    print("Hello, {}".format(player_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    need_next_question = True
    step = 0
    while need_next_question and step < 3:
        step += 1
        parity = new_question()
        print('Question: ' + str(parity))
        answer = prompt.string("Your answer: ")
        if answer.lower() == correct_answer(parity):
            print('Correct')
        else:
            template_message = "'{}' is wrong answer.\nLet's try again, {}!"
            print(template_message.format(answer, player_name))
            need_next_question = False
    if need_next_question:
        print('Congratulations, ' + player_name + '!')
