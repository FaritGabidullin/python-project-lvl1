#!/usr/bin/env python
import random
from ..game_engine import engine


def progression_game():
    numbers_count = random.randint(6, 10)
    progresser = random.randint(1, 10)
    position_for_find = random.randint(0, numbers_count - 1)
    first_number = random.randint(1, 20)
    question = ''
    for iterator in range(0, numbers_count):
        if iterator == position_for_find:
            answer = str(first_number + progresser * iterator)
            question += ".. "
        else:
            question += str(first_number + progresser * iterator) + " "
    return {'question': question, 'answer': answer}


def start_game():
    instruction = 'What number is missing in the progression?'
    engine(instruction, progression_game)
