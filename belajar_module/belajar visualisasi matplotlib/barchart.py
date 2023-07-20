import matplotlib.pyplot as plt
import csv
from collections import Counter
import pandas as pd
with open('assets/data/data.csv') as f:
    csv_reader = csv.DictReader(f)
    language_counter = Counter()
    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))

language= []
num_users = []

for data in language_counter.most_common(15):
    language.append(data[0])
    num_users.append(data[1])

# for index, row in enumerate(language):
#     print(index, row)
language[11] = 'Others Language'
language.reverse()
num_users.reverse()
print(language)
print(num_users)

plt.style.use('ggplot')
plt.barh(language, num_users)
plt.title("Most Popular Languages")
plt.ylabel("Programming Language")
plt.xlabel("Number of people who use")
plt.tight_layout()
plt.show()


