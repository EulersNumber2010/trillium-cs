import random as rnda

ubound, lbound = 100, 0

def rng(high: int, low: int):
    return rnda.randint(lbound, ubound)

if __name__ == "__main__":
    guess = int(input(f"Enter a target between {lbound} and {ubound}: "))