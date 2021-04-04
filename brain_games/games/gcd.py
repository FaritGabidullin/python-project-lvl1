#!/usr/bin/env python
import random
from math import gcd
from ..game_engine import engine


def start_game():
    def instruction():
        return 'Find the greatest common divisor of given numbers.'

    def gcd_game():
        random.seed()
        first_var = random.randint(1, 99)
        second_var = random.randint(1, 99)
        gcd_var = gcd(first_var, second_var)
        question = '{} {}'.format(str(first_var), str(second_var))
        answer = str(gcd_var)
        return {'question': question, 'answer': answer}
    engine(instruction(), gcd_game)
