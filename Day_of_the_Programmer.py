import math
import os
import random
import re
import sys

# Complete the dayOfProgrammer function below.
def conver_to_date (year,objetive, leap_year):
    mouths = [31,28,31,30,31,30,31,31,30,31,30,31]
    total, i = 0, 0
    if leap_year: mouths[1] = 29
    
    while total+mouths[i]<objetive:
        total += mouths[i]
        i += 1
    mouth = i + 1

    if mouth < 10:
        mouth = '0'+str(mouth)
    else:
        mouth = str(mouth)
    
    day = objetive - total
    if day < 10:
        day = '0'+str(day)
    else:
        day = str(day)

    return day+"."+mouth+"."+str(year)


def gregorian_calendar(year,objetive):  
    leap_year = False
    if year%4 ==0 and (year%100!=0 or year%400== 0):
        leap_year = True
    return conver_to_date (year,objetive, leap_year)


def julian_calendar(year,objetive):
    leap_year = False
    if year%4 ==0:
        leap_year = True
    return conver_to_date (year,objetive, leap_year)   


def dayOfProgrammer(year):
    objetive = 256
    if year > 1918:
        result = gregorian_calendar(year,objetive)
    elif year <1918:
        result = julian_calendar(year,objetive)
    else:
        result = gregorian_calendar(year,objetive+13)
    return result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)
    # fptr.write(result + '\n')

    # fptr.close()