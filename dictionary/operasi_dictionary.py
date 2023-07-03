data_dict = {
    "name" : "Ibnu Topan",
    "npm" : "2010631170078",
    'nationality' : "England"
}

# menghitung panjang dictioanry dengan len()
panjang_dict = len(data_dict)

# mengecek key exist atau tidak 
key = "name"
check_key = key in data_dict
print(check_key)

# kita juga bisa mengakses atau membaca dictionary
print(data_dict["name"])
# cara diatas mengakibatkan error jika key tidak ditemukan

try:
    print(data_dict["spouse"])
except KeyError:
    print("data tidak ditemukan")

# berikut adalah cara yang baik
print(data_dict.get("spouse"))
print(data_dict.get("name"))
print(data_dict.get("spouse", "not found"))  # cek key dengan message tidak ditemukan

# merubah data dictionary
data_dict["name"] = "Ibnu Topan Adib"
data_dict["spouse"] = "Freya Jayawirdana"

print(data_dict)

## bisa juga dengan method update
## dengan method update kita bisa memodifikasi value dari dictionary secara sekaligus
## ini akan mempurmudah kita jika kita ingin mengubah banyak nilai 
data_dict.update({"name": "Ibnu Topan Adib Amrulloh"})
data_dict.update({"speciality": "King of Python", "nationality": "Indonesia"})
print(data_dict)