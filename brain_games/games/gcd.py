#!/usr/bin/env python
import random
from math import gcd
from ..game_engine import engine


def gcd_game():
    first_var = random.randint(1, 99)
    second_var = random.randint(1, 99)
    gcd_var = gcd(first_var, second_var)
    question = '{} {}'.format(str(first_var), str(second_var))
    answer = str(gcd_var)
    return {'question': question, 'answer': answer}


def start_game():
    instruction = 'Find the greatest common divisor of given numbers.'
    engine(instruction, gcd_game)
