if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    max_score = max(arr)
    while max_score == max(arr):
        arr.remove(max(arr))
    print(max(arr))