# fungsi lambda
'''
    fungsi lambda tidak menggunakan def keyword melainkan menggunakan keyword lambda 
    Sebuah fungsi lambda dapat menerima argumen dalam jumlah berapa pun, 
    namun hanya mengembalikan satu nilai expression. 
    Fungsi Lambda tidak dapat memuat perintah atau ekspresi lainnya, misalnya tidak bisa melakukan print.
'''

#example

luas_segitiga = lambda alas, tinggi: (alas*tinggi)/2
luas_persegi = lambda sisi: sisi * sisi

def callfn():
    print(luas_segitiga(10, 12))
    print(luas_persegi(10))

callfn()