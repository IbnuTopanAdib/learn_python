def fibonacci (user_input):
    deret = []
    n1 = 0
    n2 = 1
    for i in range(1, user_input):
        deret.append(n1)
        bilangan_terakhir = n1 + n2
        n1 = n2
        n2 = bilangan_terakhir
    return deret

print(fibonacci(10))