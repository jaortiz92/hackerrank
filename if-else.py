import math
import os
import random
import re
import sys
def how_is_n(n):

    if n%2 != 0 or (n>=6 and n<=20):
        return "Weird"
    elif (n >=2 and n <=5) or (n>20 and n<=100):
        return "Not Weird"

if __name__ == '__main__':
    n = int(input().strip())
    print(how_is_n(n))