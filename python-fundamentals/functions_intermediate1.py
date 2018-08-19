# [ Functions Intermediate I - Objectives ] 
# =========================================
# <> Go a bit more in depth on functions

# Function: randInt():
# -------------------
# => Shall return a random integer between 0 to 100 if randInt()
# => Shall return a random integer between 0 to 50 if randInt(max=50)
# => Shall return a random integer between 50 to 100 if randInt(min=50) 
# => Shall return a random integer between 50 and 500 if randInt(min=50, max=500) 

import random

def randInt(min=0, max=100):
    return int(random.uniform(min, max))

print ("\nThe random integer between 0  to 100: ", randInt())
print ("\nThe random integer between 0  to  50: ", randInt(max=50))
print ("\nThe random integer between 50 to 100: ", randInt(min=50))
print ("\nThe random integer between 50 to 500: ", randInt(min=50, max=500))
print ("\n")


