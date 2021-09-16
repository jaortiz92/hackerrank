import math
import os
import random
import re
import sys
import collections

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    counter = dict(collections.Counter(arr))
    counter = dict(sorted(counter.items()))
    result = max(counter, key=lambda k: counter[k])
    return result

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()