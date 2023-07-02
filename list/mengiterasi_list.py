heroes = ["Kagura", "Freya", "Eudora"]
for hero in heroes:
    print(hero)

# sama seperti bahasa pemrograman lain
print("\nSama seperti bahasa pemrograman lain")
panjang = len(heroes)

for i in range(panjang):
    print(heroes[i])

# while 
print("\nmenggunkan While")
panjang = len(heroes)
i = 0
while i < len(heroes):
    print(heroes[i])
    i+=1
# menggunakan list comprehension 
print("\nmenggunkan list comprehension")
[print(f"nama {hero}") for hero in heroes]

# menggunakan enumerate()
for index, value in enumerate(heroes):
    print("{} {}".format(index, value))

