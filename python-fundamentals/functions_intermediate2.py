# ==========================================
# [ Functions Intermediate II - Objectives ] 
# ==========================================
# <> Learn how to write functions and looping over dictionaries
# <> Learn how to traverse through an array of dictionaries 
#    or dictionary of arrays


# Task #1:
#---------
# <> Change the value 10 in x to 15
# <> Once you're done x should then be [ [5,2,3], [15,8,9] ].
print ("\nTask 1.1:\n---------")
x = [ [5,2,3], [10,8,9] ] 
print ("Array x before being updated: ", x)

x[1][0]=15
print ("Array x after being  updated: ", x)


# Task #2:
#---------
# <> How would you change the last_name of the first student from 'Jordan' to "Bryant"?
print ("\nTask 1.2:\n---------")
students = [{
    'first_name': 'Michael', 
    'last_name' : 'Jordan'
},
{
    'first_name': 'John',
    'last_name' : 'Rosales'
}]
print ("Students Dict. before being updated: ", students)
for student in students:
    if (student == 'Jordan'):
        students['first_name'] = 'Bryant'
print ("Students Dict. after being updated: ", students)


# Task #3:
#---------
# <> For the sports_directory, how would you change 'Messi' to 'Andres'?
print ("\nTask 1.3:\n---------")
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
print ("Sports Dict. before being updated: ", sports_directory)
for sport in sports_directory:
    k=0
    for player in sports_directory[sport]:
        if (player == 'Messi'):
            sports_directory[sport][k] = 'Andres'
        k += 1
print ("Students Dict. after being updated: ", sports_directory)


# Task #4:
#---------
# <> For z, how would you change the value 20 to 30?
print ("\nTask 1.4:\n---------")
z = [ {'x': 10, 'y': 20} ]
print ("Array z before being updated: ", z)

z[0]['x'] = 30
print ("Array z after being  updated: ", z)



print ("\n\n"
        "============================\n"
        "|        FUNCTIONS         |\n"
        "============================\n")

# Function 1: Navigate through and prints dictionaries
# ----------------------------------------------------
# => Shall take in a list of dictionaries, 
# => Shall loop through each dictionary in the list and print each key and the associated value.

def iterateDictionary1( dictionaries ):
    # Check if the list of dictionary is empty
    if (len(dictionaries) < 1):
        return False
    
    # Continue with task
    for _dict in dictionaries:
        for item in _dict:
            print ("\t",item + " - " + _dict[item], end="")
        print (", ")

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
print ("=> Function #1 outputs: List of keys and associated value from dictionaries:"
       "\n\n\tFirstKey - Value\t SecondKey - Value"
       "\n\t-------------------------------------------")
iterateDictionary1( students )
print("\n")




# Function 2: iterateDictionary2() 
# --------------------------------
# Shall take in a list of dictionaries and a key name
# Shall output the value stored in that key for each dictionary.  
# => Ex: iterateDictionary2('first_name', students) should output 
#        Michael
#        John
#        Mark

def iterateDictionary2( dictionaries, key ):
    # Check if the list of dictionary is empty
    if (len(dictionaries) < 1):
        return False
    
    # Continue with task
    for _dict in dictionaries:
        for _key in _dict:
            if _key == key:
                print ("\t", _dict[_key])

print ("=> Function #2 outputs: List of values associated to a given key from dictionaries:"
       "\n\n\tGiven key <'first_name'>"
       "\n\t--------------------------")
iterateDictionary2( students, 'first_name' )




# Function 3: 
#------------
# Shall print the name and number of each location that Coding Dojo currently has.
# Shall print the name and number of each instructor that Coding Dojo currently has. 
# => Ex: printDojoInfo(dojo) should output

def printDojoInfo( dojo ):
    # Check if the list of dictionary is empty
    if (len(dojo) < 1):
        return False
    
    # Continue with task
    count = 0
    print ("\n\t"+ str(len(dojo['location'])) +" Locations"
           "\n\t-----------")
    for _list in dojo:
        for k in dojo[_list]:
            print ("\t" + k)
        print (" ")
        count += 1
        if (count < len(dojo)):
            print ("\t"+ str(len(dojo['instructors'])) +" Instructors"
                   "\n\t-------------")

dojo = {
   'location': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

print ("\n=> Function #3 outputs: List of keys and associated value from dictionaries:")

printDojoInfo( dojo )
