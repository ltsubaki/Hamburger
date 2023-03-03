# Lilian Tsubaki, Danny Wright, Aiki Takaku, Maya Sakuma, Rylan Rawson, Ryan Ward

# This code generates random names associated with a number of burgers to a single customer
# It then generates a queue of 100 customers
# It creates a running total of the number of burgers each customer orders within a dictionary,
# then sorts the customers in descending order of burgers ordered
# The code out this sorted list in a aesthetic format

from random import randint

# Order class to generate random burger count
class Order :
    def __init__(self) :
        self.burger_count = 0
        self.burger_count = self.randomBurgers()

    def randomBurgers(self) :
        return randint(1, 20)

# Person class to generate random name
class Person :
    def __init__(self) :
        self.customer_name = self.randomName()

    def randomName(self) :
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", 
                       "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return self.asCustomers[randint(0,8)]

# Customer class that inherits from person class
# Gives each person an order  
class Customer(Person) :
    def __init__(self):
        super().__init__()
        self.order = Order()

# Create customer queue
customerQueue = []

# Create dictionary
dictCustomer = {}

# Create queue of 100 customers
for iCount in range (0, 100) :
    oCustomerQueue = Customer()
    customerQueue.append(oCustomerQueue)
    # USE NEXT LINE FOR DEBUG
    # print(customerQueue[iCount].customer_name)

# Add burgers to running total
for iLine in range (0, len(customerQueue)) :
    # If the customer is already in the dictionary, add to their total
    if customerQueue[0].customer_name in dictCustomer :
        dictCustomer[customerQueue[0].customer_name] = dictCustomer[customerQueue[0].customer_name]\
        + customerQueue[0].order.burger_count
    # If the customer isn't in the dictionary yet, add them with burger total
    else :
        dictCustomer[customerQueue[0].customer_name] = customerQueue[0].order.burger_count

    # Pop the customer to help next customer!
    customerQueue.pop(0)

# USE NEXT LINE FOR DEBUG
# print(dictCustomer)

# Sort the dictionary from largest value to smallest
listSortedCustomers = sorted(dictCustomer.items(), key=lambda x: x[1], reverse=True) 

# USE NEXT LINE FOR DEBUG
# print(listSortedCustomers)

# For loop to output each customer and accompanying value
for lstCount in range (0, len(listSortedCustomers)) :
    customer = listSortedCustomers[lstCount]

    print(customer[0].ljust(19) + str(customer[1]))
