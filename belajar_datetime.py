import datetime as dt

class Biodata:
    def __init__(self, name, height , weight, *, birthday = 0, birthmonth = 0, birthyear =0):
        self.name = name
        self.height = height
        self.weight = weight
        self.birthday = birthday
        self.birthmonth = birthmonth
        self.birthyear = birthyear
    def define_age(self):
        birth = dt.date(self.birthyear, self.birthmonth, self.birthday)
        now = dt.date.today()
        age_now_days = now - birth
        age_now_year = age_now_days.days/365
        return age_now_year


ibnu = Biodata("Ibnu Topan", 165, 50,birthday = 5,
               birthmonth=5, birthyear =2001)
umur_ibnu = ibnu.define_age()
print(ibnu.name)
print(umur_ibnu)





