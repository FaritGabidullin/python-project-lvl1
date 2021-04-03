#!/usr/bin/env python
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def engine(instruction, game):
    def question(inner_game):
        return inner_game['question']

    def correct_answer(inner_game):
        return inner_game['answer']
    player_name = welcome_user()
    print("Hello, {}".format(player_name))
    print(instruction)
    need_next_question = True
    step = 0
    while need_next_question and step < 3:
        step += 1
        one_game_object = game()
        print('Question: ' + question(one_game_object))
        answer = prompt.string("Your answer: ")
        if answer.lower() == correct_answer(one_game_object):
            print('Correct')
        else:
            template_message = "'{}' is wrong answer ;(. Correct answer was {}."
            print(template_message.format(
                answer, correct_answer(one_game_object)))
            print("Let's try again, {}!".format(player_name))
            need_next_question = False
    if need_next_question:
        print('Congratulations, ' + player_name + '!')
