import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # m, n = 0,0
    # for i in apples:
    #     if a + i >= s and a + i <= t:
    #         m += 1
    # for i in oranges:
    #     if b + i >= s and b + i <= t:
    #         n += 1
    # return m,n 
    return sum(s<=a+i<=t for i in apples ),sum(s<=b+i<=t for i in oranges)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    m, n = countApplesAndOranges(s, t, a, b, apples, oranges)
    print(m)
    print(n)