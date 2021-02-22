# com_funcs.py
"""
com_funcs.py is a Python module that contains some communication functions
"""

from math_funcs import plus_two

def say_hi(name):
    out = f"Hi {name}!"
    return out

def say_hi_to_plus_two(number):
    number_plus2 = plus_two(number)
    out = say_hi(number_plus2)
    return out
