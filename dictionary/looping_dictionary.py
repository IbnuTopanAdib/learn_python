data_dict = { 'name': 'Ibnu Topan Adib Amrulloh', 
             'npm': '2010631170078', 
             'nationality': 'Indonesia', 
             'spouse': 'Freya Jayawirdana', 
             'speciality': 'King of Python'
             }
# kita bisa mengiterasi dictionary dengan keynya dengan method keys()
key_dict = data_dict.keys()
print(key_dict)
for key in data_dict.keys():
    print(f"key: {key}")

# apakah kita bisa melakukan enumerate?

for index, key in enumerate(data_dict.keys()):
    print(f"index: {index} | key: {key}")

# kita bisa mengiterasi dictionary dengan keynya dengan method values()
print(data_dict.values())

for value in data_dict.values():
    print(f"value-> {value}")


# ini adalah yang paling powerful kita bisa mengiterasi dictionary dengan key dan valuenya dengan method items()
print(data_dict.items())

for key, value in data_dict.items():
    print(f"key :{key} | value :{value}")