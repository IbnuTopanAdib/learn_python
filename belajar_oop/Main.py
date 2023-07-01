class Hero:
    #class variable/ static variable
    jumlah = 0
    heal_max = 2.0
    def __init__(self,input_name, input_health, input_power, input_armor):
        #instance variabel/ attribute
        self.name =  input_name
        self.health= input_health
        self.att_power = input_power
        self.armor = input_armor
        Hero.jumlah+=1
        print(f"Membuat hero dengan nama {input_name} ")
    #void function/ fungsi yang tidak punya argument dan return
    def who(self):
        print(f'Hi Adventurer my Name is {self.name}')
    # fungsi dengan argumen
    def healthUp(self):
        self.health += Hero.heal_max
    #fungsi return
    def getHealth(self):
        return self.health
    def attack(self, enemy):
        print(f"{self.name} menyerang {enemy.name}")
        enemy.defender(self, self.att_power)

    def defender(self, enemy, enemy_att_power):
        print(f"{self.name} diserang {enemy.name}")
        acq_attack = enemy_att_power/self.armor
        print(f"serangan diterima {acq_attack}")
        self.health -= acq_attack
        print(f"HP {self.name} sekarang adalah {self.health}")







ibnu = Hero("Ibnu", 200,12, 50)

lunglee = Hero("Lunglee", 100, 100, 20)

lunglee.who()
ibnu.who()
lunglee.attack(ibnu)
print()
ibnu.attack(lunglee)


