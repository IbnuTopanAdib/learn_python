# method join dan method strip

''' menurutku method join dan method strip adalah
 method yang paling sering digunakan dalam oprasi 
 string'''

data_pemain = ["cr7", "lionel messi", "neymar"]

kalimat = ' dan '.join(data_pemain) + " adalah pemain bola terhebat di abad 21"

print(kalimat)

nama = ["ibnu", "topan"]

print(' '.join(nama))


makanan = "sate, nasi, rendang, bakso"

makanan = makanan.split(",")

print(makanan)

print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))