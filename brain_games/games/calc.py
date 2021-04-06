#!/usr/bin/env python
import random
from ..game_engine import engine


def calc_game():
    first_var = random.randint(1, 99)
    second_var = random.randint(1, 99)
    operation = random.randint(1, 3)
    if operation == 1:
        question = '{} + {}'.format(str(first_var), str(second_var))
        answer = str(first_var + second_var)
    if operation == 2:
        question = '{} - {}'.format(str(first_var), str(second_var))
        answer = str(first_var - second_var)
    if operation == 3:
        question = '{} * {}'.format(str(first_var), str(second_var))
        answer = str(first_var * second_var)
    return {'question': question, 'answer': answer}


def start_game():
    instruction = 'What is the result of the expression?'
    engine(instruction(), calc_game)
