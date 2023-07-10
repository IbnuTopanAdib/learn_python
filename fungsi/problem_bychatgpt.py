mahasiswa = ["John,85", "Alice,76", "Bob,92", "Charlie,80", "Eva,88"]

nilai = lambda x: int(x.split(",")[1])


mahasiswa.sort(key = nilai)

print(mahasiswa)


students = [("John", 21, 175), ("Alice", 20, 163), ("Bob", 22, 180), ("Charlie", 19, 168)]
print(students[1])
usia = lambda x: x[1]


list_saya = [
    {
        "nama" : "ibnu",
        "umur" : 21
    },
        {
        "nama" : "john",
        "umur" : 58
    },
            {
        "nama" : "taylor swift",
        "umur" : 33
    },
]
def age (x: list):
    return x["umur"]
list_saya.sort(key = age)

print(list_saya)



