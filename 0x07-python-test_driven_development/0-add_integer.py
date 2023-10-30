#!/usr/bin/python3

def add_integer(a, b=98):
    """
    add_integer: Add two integers together

    Parameter: 
        a = first integer to add
        b = second integer to add

    Return: 
        The addition of the two integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    result = int(a) + int(b)
    return result