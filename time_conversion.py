import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    hour = int(s[:2])
    letter = s[-2]
    if letter =="A" and hour == 12:
        s ="00"+s[2:8]
    elif letter =="A" or hour == 12:
        s = s[:8]
    else:
        s =str(hour+12)+s[2:8]
    return s

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)

    # f.write(result + '\n')

    # f.close()
