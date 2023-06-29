class Apaya:
    def __init__(self, * , name, income):
        self.name = name
        self.income = income
    def __str__(self):
        return f"{self.name}, {self.income}"