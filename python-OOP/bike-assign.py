# ================
# Assignment: Bike
# ================

# Objectives:
# ==========================================================
# <>  Practice creating a class and making instances from it
# <>  Practice accessing the methods and attributes of different instances
# ========================================================================

class Bike:
    def __init__(self, price, max_speed, miles):
        self.price = 0 if price <= 0 else price
        self.speed = int(max_speed[:-3])
        self.miles = miles

    def displayInfo(self):                   # => displays the bike's price, 
                                             #    maximum speed, and miles.
        print (f"Price: {self.price}\tMax. Spped: {self.speed}mph\tMiles: {self.miles}")

    def ride(self, name='', runcount=1):     # => displays "Riding" on the screen and 
        while (runcount > 0):                #    increase the total miles ridden by 10
            self.speed += 10
            runcount -= 1
            print (f"{name}    Riding at:  {self.speed}mph")
        return self

    def reverse(self, name='', runcount=1):  # => displays "Reversing" on the screen a
        while (runcount > 0):                #    nd decrease the total miles ridden by 5
            self.speed -= 5
            runcount -= 1
            print (f"{name} Reversing by:  {self.speed}mph")
        return self


bike1 = Bike(100, "10mph", 10000)   # instantiate bike1
bike2 = Bike(200, "20mph", 20000)   # instantiate bike2
bike3 = Bike(300, "30mph", 30000)   # instantiate bike3

# bike1 actions
print()
bike1.ride("bike1", 3)
bike1.reverse("bike1")
#
# # bike2 actions
print()
bike2.ride("bike2", 2)
bike2.reverse("bike2", 2)

# bike3 actions
print()
bike2.reverse("bike2", 2)
