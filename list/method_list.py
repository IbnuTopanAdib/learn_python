
# indexing list
mylist = ["Ibnu", "Freya", "Khufra"]
#          0/-3     1/-2     2/-1
print(mylist[0])
print(mylist[1])
print(mylist[-1])

is_sama = mylist[2] == mylist[-1]
print(is_sama)

# method insert untuk memasukan elemen sesuai index yang diberikan
## list.(index, element)
mylist.insert(2, "kagura")
print(mylist)

# menentukan panjang list dengan len()
print(len(mylist))

# menambah list diujung dengan append()
mylist.append("Yve")
print(mylist)

# merubah element list

mylist[2] = "Kagura"
print(mylist)

# menambah list dengan list baru dengan extend
mynewlist = ["Pharsa", "Franco", "Chou"]
mylist.extend(mynewlist)
print(mylist)

# menghapus element list dengan remove
mylist.remove("Franco")


# mengeluarkan elemnt terakhir list dengan method pop()
hasil_pop = mylist.pop()
print(mylist)
print(hasil_pop)
