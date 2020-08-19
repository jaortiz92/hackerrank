if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key, valor in student_marks.items():
        if key == query_name:
            print("{0:.2f}".format(sum(valor)/len(valor)))