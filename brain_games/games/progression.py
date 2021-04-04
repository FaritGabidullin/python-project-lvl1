#!/usr/bin/env python
import random
from ..game_engine import engine


def start_game():
    def instruction():
        return 'What number is missing in the progression?'

    def gcd_game():
        random.seed()
        numbers_count = random.randint(5, 10)
        progresser = random.randint(1, 10)
        position_for_find = random.randint(0, numbers_count - 1)
        first_number = random.randint(1, 20)
        question = ''
        for iterator in range(0, numbers_count):
            if iterator == position_for_find:
                answer = str(first_number + progresser * iterator)
                question += " .."
            else:
                question += " " + str(first_number + progresser * iterator)
        return {'question': question, 'answer': answer}
    engine(instruction(), gcd_game)
