if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(student_marks)
    hasil = 0
    for name, value in student_marks.items():
        if name == query_name:
            for i in value:
                hasil += i
                rata = hasil/ float(len(value))

    print(rata)