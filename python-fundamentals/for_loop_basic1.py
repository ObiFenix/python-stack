#===================
# For Loop Basic I |
#===================

# Basic
print ("\n"
       "\nPrint all the numbers/integers from 0 to 150:"
       "\n---------------------------------------------"
       "\n=> Result: [", end=" ")
for i in range(51):
    print ("%s" % i, end=" "),
print ("]")
    
    
# Multiples of Five
print ("\n"
       "\nPrint all the multiples of 5 from 5 to 1,000,000:"
       "\n-------------------------------------------------"
       "\n=> Result: [", end=" "),
for i in range(5, 51):
    if (i % 5 == 0):
        print ("%d" % i, end=" "),
print ("]")


# Counting, the Dojo Way
print ("\n"
       "\nPrint integers 1 to 100."
       "\n  <> If divisible by 5, print 'Coding'"
       "\n  <> If divisible by 10 print 'Dojo':"
       "\n-------------------------------------"
       "\n=> Result: [", end=" "),
for i in range(1, 101):
    if (i % 10 == 0):
        print ("%s" % 'Dojo,', end=" "),
    elif (i % 5 == 0):
        print ("%s" % 'Coding', end=" "),
    else:
        print(i, end=" "),
print ("]")


#Whoa. That Sucker's Huge
print ("\n"
       "\nAdd odd integers from 0 to 500,000, and print the final sum:"
       "\n------------------------------------------------------------"
       "\n=> Result: ", end=" "),
sum = 0
for i in range(50):
    if (i % 2 != 0):
        sum = sum + i
print(sum)


# Countdown by Fours
print ("\n"
       "\nPrint positive numbers starting at 2018, counting down by fours (exclude 0):"
       "\n----------------------------------------------------------------------------"
       "\n=> Result: [", end=" "),
N = 2018
while (N > 0):
    print ("%d" % N, end=" "), 
    N -= 400
print ("]"),


# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult,
# Print multiples of mult from lowNum to highNum, using a FOR loop.  For (2,9,3), print 3 6 9 (on successive lines)
mult = -4
lowNum = 1
highNum = 20
print ("\n"
       "\nPrints flexible countdown of multiples of 4"
       "\ngiven sizes of lowest number and max. number:"
       "\n---------------------------------------------"
       "\n=> Result: [", end=" "),
for i in range(highNum, lowNum, mult):
    print (i, end=" "),
print ("]\n"),
