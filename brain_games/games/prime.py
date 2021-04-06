#!/usr/bin/env python
import random
from ..game_engine import engine


def prime_game():
    def isPrime(n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n
    random.seed()
    question_number = random.randint(1, 99)
    answer = 'no'
    if isPrime(question_number):
        answer = 'yes'
    question = str(question_number)
    return {'question': question, 'answer': answer}


def start_game():
    instruction = (
        'Answer "yes" if given number is prime. Otherwise answer "no".')
    engine(instruction, prime_game)
