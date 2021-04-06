#!/usr/bin/env python
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def engine(instruction, game):
    player_name = welcome_user()
    print("Hello, {}\n{}".format(player_name, instruction))
    need_next_question = True
    step = 0
    while need_next_question and step < 3:
        step += 1
        one_game_object = game()
        print('Question: ' + one_game_object['question'])
        answer = prompt.string("Your answer: ")
        if answer.lower() == one_game_object['answer']:
            print('Correct')
        else:
            template_message = "'{}' is wrong answer ;(. Correct answer was {}."
            print(template_message.format(
                answer, one_game_object['answer']))
            print("Let's try again, {}!".format(player_name))
            need_next_question = False
    if need_next_question:
        print('Congratulations, ' + player_name + '!')
