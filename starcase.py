import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    string = '#'
    espace = ' '
    for i in range(n,-1,-1):
        print(f'{espace*(i)}{string*(n-i)}')

def staircase1(n):
    string = '#'
    espace = ' '
    for i in range(n):
        print(f'{espace*(n-i-1)}{string*(i+1)}')

if __name__ == '__main__':
    n = int(input())

    staircase(n)