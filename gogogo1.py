if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])

    arr.sort(key=lambda x: (x[1], x[0]))

    second_lowest_score = None
    for i in range(1, len(arr)):
        if arr[i][1] > arr[0][1]:
            second_lowest_score = arr[i][1]
            break

    second_lowest_names = []
    for student in arr:
        if student[1] == second_lowest_score:
            second_lowest_names.append(student[0])

    second_lowest_names.sort()

    for name in second_lowest_names:
        print(name)

