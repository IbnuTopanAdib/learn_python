
input_user = int(input("masukan angka"))

def bilangan_genap(angka):
    x = angka if angka%2 == 0 else "zonk"
    return x

output = bilangan_genap(input_user)

print(output)


