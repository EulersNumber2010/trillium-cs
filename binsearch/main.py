import random as rnda
import time as t

ubound, lbound = 100, 0

def rng(high: int, low: int):
    return rnda.randint(lbound, ubound)

target = int(input(f"Choose a target between {lbound} and {ubound}: "))

starttime = t.perf_counter()
while True:
    guess = (ubound + lbound) // 2
    if target > guess:
        lbound = guess
        print("higher")
    elif target < guess:
        ubound = guess
        print("lower")
    elif target == guess:
        endtime = t.perf_counter()
        print(guess)
        print(endtime - starttime)
        break