if __name__ == '__main__':
    x = [x for x in range(int(input())+1)]
    y = [y for y in range(int(input())+1)]
    z = [z for z in range(int(input())+1)]
    n = int(input())

    # list_number = [[i,j,k] for i in x for j in y for k in z]
    # print([x for x in list_number if sum(x) != n])
    print([[i,j,k] for i in x for j in y for k in z if i+j+k != n])