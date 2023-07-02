# membuat list
my_list = ["ibnu", "freya", "khufra", "lolita"]

# membuat list comprehension

bilangan_genap = [ x for x in range(1, 10) if x % 2 == 0]
print(bilangan_genap)

bilangan_ganjil = [ x for x in range(1, 10) if x % 2 != 0]
print(bilangan_ganjil)

bilangan_kuadrat = [ x**2 for x in range(1, 10)]


