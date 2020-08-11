import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    tamano = len(arr)
    a = []
    b = []
    j  = 1
    for i in arr:
        a.append(i[tamano-j])
        b.append (i[j-1])
        j += 1
           
    return abs(sum(a)-sum(b))
    


if __name__ == '__main__':
    

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print (result)