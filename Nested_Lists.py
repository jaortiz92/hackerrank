if __name__ == '__main__':
    name, score,lists=[],[],[]
    for _ in range(int(input())):
        name.append(input())
        score.append(float(input()))
    min_score = min(score)
    
    while min_score == min(score):
        name.pop(score.index(min(score)))
        score.remove(min(score))
    min_score = min(score)
    
    for i,j  in zip(name,score):
        if min_score == j:
            lists.append(i)
    lists.sort()
    
    for i in lists:
        print(i)

    # a= []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     a.append([score, name])

    # a.sort()
    # b = [i for i in a if i[0] != a[0][0]]
    # c = [j for j in b if j[0] == b[0][0]]
    
    # c.sort(key=lambda x: x[1])
    # for i in range(len(c)):
    #     print(c[i][1])