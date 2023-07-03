biodata = { 'name': 'Ibnu Topan Adib Amrulloh', 
             'npm': '2010631170078', 
             'nationality': 'Indonesia', 
             'spouse': 'Freya Jayawirdana', 
             'speciality': 'King of Python'
             }
# sama seperti list kita menggunakan method copy() untuk mengcopy dctionary

biodata_baru = biodata.copy()

print("biodata_baru: {}\n".format(biodata_baru))
print("biodata_lama: {}\n".format(biodata))

# misalkan kit mau merubah data biodata baru apakah biodata lama akan berubah?
biodata_baru.update({"speciality": "king of Reactjs"})
print("biodata_lama: {}\n".format(biodata))
print("biodata_baru: {}\n".format(biodata_baru))

# ternyata tidak berarti kita sudah bisa mengcopy biodata lama

# pop pada dictionary akan mengeluarkan value dari key yang kita berikan 
data_pasangan = biodata_baru.pop('spouse')
print("data pasangan : {}".format(data_pasangan))
print("biodata_baru: {}\n".format(biodata_baru))

# pop_item pada dictionary akan mengeluarkan value dar
item = biodata_baru.popitem()
print(item)
print("biodata_baru: {}\n".format(biodata_baru))