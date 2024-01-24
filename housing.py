class House:
    totalNumHouse = 0

    def __init__(self, owner, condition, price):
        self.owner = owner
        self.price = price
        self.condition = condition
        self.cost = 0
        self.sold = False
        House.totalNumHouse += 1

    @classmethod
    def totalHouses(cls):
        print(f"There are {cls.totalNumHouse} houses.")

    def sell(self, newOwner, cost):
        self.cost = cost
        self.owner = newOwner
        self.sold += 1
        self.sold = True
        profit = self.cost - self.price
        print(f"SOLD!  Profit = ${profit}")

    def changePrice(self, newPrice):
        if self.sold == True:
            print("House has been sold!")
        else:
            self.price = newPrice

    def renovate(self, expenses, new_condition):
        self.price = expenses + self.price
        self.condition = new_condition
        print("House renovated!")

    def printInfo(self):
        print(
            f"""
Owner: {self.owner}
Condition: {self.condition}
Price: ${self.price}
""")

#make houses name, condition, price
h1 = House("John", "Good", 100000)
h2 = House("Sara", "Bad", 250000)
#house info
h1.printInfo()
h2.printInfo()
#renovate for 5000 and set new condidion
h1.renovate(5000, "Great")
#sell house, new owner, price paid
h1.sell("Leo", 200000)
h1.printInfo()
print(f"Total number of houses: {House.totalNumHouse}")