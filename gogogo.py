if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    angka_list = []
    # should output [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if ((i + j + k)!= n):
                   angka_list.append([i, j , k])

    print(angka_list)