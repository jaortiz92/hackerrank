import sys

if __name__ == '__main__':
    n = int(input())
    # lists = ""
    # for i in range(1,n+1):
    #     lists += str(i)
    print(*range(1, n+1), sep='')