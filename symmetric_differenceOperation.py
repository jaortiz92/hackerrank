

def diferencelist(set1,set2):
    print (len(set1.symmetric_difference(set2)))

if __name__ == "__main__":
    en_count = int(input())
    en = set(map(int, input().rstrip().split()))
    fr_count = int(input())
    fr = set(map(int, input().rstrip().split()))
    diferencelist(en, fr)