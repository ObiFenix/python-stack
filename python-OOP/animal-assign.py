# ==================
# Assignment: Animal
# ==================

# Objectives:
# ==============================================
# <> Shall be able to inherit from another class
# <> Shall be able to customize children classes
# <> Shall have children classes call methods from the parent class
# =================================================================

class Animal:
    def __init__ (self, name, health):
        self.name = name
        self.health = health if (isinstance (health,int) and health >= 0) else None
    def walk (self, runcount=1):
        if runcount < 1:               return
        for count in range(runcount):  self.health -= 1
        if (self.health < 0):  self.health = 0
        return self
    def run (self, runcount=1):
        if runcount < 1:               return
        for count in range(runcount):  self.health -= 5
        if (self.health < 0):  self.health = 0
        return self
    def display_health (self):
        if ( isinstance (self, Dragons) ):
            output = f"Name: {self.name}\t\tHealth: {self.health}\tI am a Dragon"
        else:
            if (len(self.name) > 6): output = f"Name: {self.name}\tHealth: {self.health}"
            else:                    output = f"Name: {self.name}\t\tHealth: {self.health}"
        print(output)
        return self

class Dog (Animal):
    def __init__ (self, name):
        super().__init__ (name, 150)  # Applies <super> to call the Animal __init__() method
    def pet (self):
        self.health += 5     # shall increase the health of any dog by 5

class Dragons (Animal):
    def __init__ (self, name):
        super().__init__ (name, 170)
    def fly (self):
        self.health -= 10
        self.display_health ()


# ==============================
# [        Main Section        ]
# ==============================
if (__name__ == '__main__'):
    
    animal = Animal ('Jose Cuervo', 10)
    print ("\nAnimals:\n" + "-"*len('Animals:'))
    animal.walk ( 3 )
    animal.run ( 2 )
    animal.display_health ()
    print ()

    dog = Dog ('Bolt')
    dog.walk ( 3 )
    dog.run ( 2 )
    dog.display_health ()
    print ()

    dragon = Dragons('Shenron')
    dragon.walk ( 3 )
    dragon.run ( 2 )
    dragon.fly ()
    dragon.display_health ()
    print ()
