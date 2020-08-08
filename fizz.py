#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    i = 1
    for i in range(1,n):
        if (i % 3 == 0 and i % 5 == 0):
            print(f"FizzBuzz")
            continue
        elif (i % 3 == 0 and i % 5 is not 0):
            print("FIZZ")
            continue
        elif (i % 5 == 0 and i % 3 is not 0):
            print("Buzz")
            continue
        else:
            print(i)
            continue

if __name__ == '__main__':
    n = int(input("ENTER NUMBER"))
    fizzBuzz(n)


