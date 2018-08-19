# ================
# Assignment: Cars
# ================

# Objectives:
# =============================================================
# <>  Shall allow the user to specify the following attributes:
#     o  price      o  speed      o  fuel      o  mileage
# -------------------------------------------------------------------------
# <>  Shall set the tax to 15% if the price > 10,000; otherwise, set it 12%
# <>  Shall have six different instances of the class Car.
# <>  Shall have a method that returns all the car information as a string
# =========================================================================

class Car:

    taxes = .12
    
    def __init__(self, name, price, speed, fuel, mileage):
        self.name = name
        self.fuel = fuel
        self.speed = speed
        self.mileage = mileage
        self.price = 0 if price <= 0 else price
        print ()
        self.tax()
        print (self.displayAll())

    def displayAll(self):
        underline = "-"*len(self.name)
        return "{}{}\nPrice: {}\tMax. Spped: {}mph\tMileage: {}\tTax: {}".format(
            self.name,
            underline,
            self.price,
            self.speed,
            self.mileage,
            self.taxes)

    def tax(self):
        if (self.price > 10000):
            self.taxes += self.taxes + .03
        return self

# Siz instances of Car
# --------------------
Lexus  = Car("Lexus\n", 45000, 15, 'Full', 95)
Honda  = Car("Honda\n", 20000, 30, 'Full', 15)
Dodge  = Car("Dodge\n", 12000, 45, 'Empty', 25)
Volvo  = Car("Volvo\n", 8500, 10, 'Full', 105)
Nissan = Car("Nissa\n", 9000, 20, 'Hybrid', 25)
Tesla  = Car("Tesla\n", 9999, 35, 'Electric', 15)
