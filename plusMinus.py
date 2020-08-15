import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positive = 0
    negative = 0
    cero = 0
    for n in arr:
        if n > 0:
            positive += 1
        elif n < 0:
            negative += 1
        else:
            cero += 1
    print("{0:.6}".format(positive / len(arr)))
    print("{0:.6}".format(negative / len(arr)))
    print("{0:.6}".format(cero / len(arr)))
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)