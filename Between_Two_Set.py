
import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    max_number = max(a)
    min_numbre = min(b)
    first, last = [],[]
    for i in range(max_number,min_numbre+1): 
        count = 0
        for j in a:
            if i%j== 0:
                count += 1 
        if count == len(a):
            first.append(i)
    for i in first:
        count = 0
        for j in b:
            if j%i == 0:
                count += 1
        if count == len(b):
            last.append(i)              
    return len(last)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
    # fptr.write(str(total) + '\n')

    # fptr.close()
