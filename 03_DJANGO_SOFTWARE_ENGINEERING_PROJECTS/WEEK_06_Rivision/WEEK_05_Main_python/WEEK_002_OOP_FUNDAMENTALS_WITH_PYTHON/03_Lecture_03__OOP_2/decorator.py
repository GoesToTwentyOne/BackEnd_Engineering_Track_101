from math import *
def timer_dec(func):
    def innner_dec(*args):
        print("starting")
        func(*args)
        print("ending")
    return innner_dec
@timer_dec
def fact(n):
    print(f"factorial of {n} is {factorial(n)}")
fact(3)

