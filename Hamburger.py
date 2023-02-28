# IS 303 Group Project

from random import randint

class Order():
    def __init__(self):
        self.burger_count = ""
    def randomBurgers(self):
        randomBurgers = randint(1,20)

class Person():
    def __init__(self):
        self.customer_name = ""
            self.custumer_name = ""
    def randomName(self):
        asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return self.asCustomers[randint(0,8)]
        
print("Hello world")

