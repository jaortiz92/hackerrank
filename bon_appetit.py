import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.pop(k)
    dif =  b - int(round(sum(bill)/2))
    return dif if dif!=0 else 'Bon Appetit'

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    print(bonAppetit(bill, k, b))
