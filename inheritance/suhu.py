class Suhu:
    def __init__(self, value):
        self.value = value

    def celcius(self):
        return self.value

class Suhu2(Suhu):
    def __init__(self, value):
        self.value = value
        
    def fahrenheit(self):
        celcius = super().celcius()
        self.value = (celcius * (9/5)) + 32
        return self.value

suhu2 = Suhu2(32)
celcius = suhu2.celcius()
print(celcius)
fahrenheit = suhu2.fahrenheit()
print(fahrenheit)