import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_score,min_score = scores[0],scores[0]
    highest, lowest = 0, 0
    for score in scores:
        if score > max_score:
            highest += 1
            max_score = score
        elif score < min_score:
            lowest += 1
            min_score = score
    return [highest, lowest]    


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    
    print (*breakingRecords(scores))
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
