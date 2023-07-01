class Hero:
    def __init__(self, name, att_power, health):
        self.__name = name
        self.__att_power = att_power
        self.__health = health
    def getHealth(self):
        return self.__health
    def getAttPower(self):
        return self.__att_power
    def diserang(self, powerDiserang):
        self.__health -= powerDiserang
    def armored(self, powerarmor):
        self.__att_power -= powerarmor



hero1 = Hero("miranda", 20, 100)
print(hero1.getHealth())
hero1.diserang(12)
print(hero1.getHealth())
hero1.armored(10)
print(hero1.getAttPower())
