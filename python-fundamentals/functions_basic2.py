# [ Objectives ]
# ================================================
# <> Learn how to create basic functions in Python
# <> Get comfortable using lists
# <> Get comfortable having the function return an expression/value
# =================================================================

# Function 1: Countdown
# ---------------------
# => Create a function that accepts a number as an input.
# => Return a new array that counts down by one, from the number down to 0.
#    Ex: countDown(5) should return [5,4,3,2,1,0].
def countDown( N ):
    arr = []
    for n in range(N, -1, -1):
        arr.append(n)
    return arr

list = countDown(5)
print "\nThe Countdown list = ", list


# Function 2: Print and Return
# ----------------------------
# => shall receive an array with two numbers.
# => shall print the first value, and return the second.
def printReturn( arr ):
    print "\nThe 1st value: ", arr[0]
    return arr[-1]

second_val = printReturn([3,2])
print "The 2nd value: ", second_val


# Function 3: First Plus Length
# -----------------------------
# => shall be given an array,
# => shall return the sum of the first value in the array and the array's length.
def firstPlusLength( arr ):
    return arr[0] + len(arr)

print "\nThe sum of the 1st value in the array plus the array's length: ", firstPlusLength([2,1,4,5])
print("\n")


# Function 4: Values Greater than Second
# --------------------------------------
# => shall accept any array
# => shall returns a new array with the array values that are greater than its 2nd value.
# => shall print how many values this is.  If the array is only element long, have the function return False
def valGreaterThan2nd( arr ):
    if (len(arr) <= 1): return False

    newArr = []
    for item in arr:
        if (item > arr[1]):
            newArr.append(item)

print "Result: ", valGreaterThan2nd([2])
print("\n")


# Function 5: This Length, That Value
# -----------------------------------
# => shall be given two numbers,
# => shall return array of length num1 with each value num2.
# => shall print "Jinx!" if they are same.
arr = []
def thisLengthArr(num1, num2):
    for k in range(0, num1):
        if (k < num2):
            arr.append(k)
        else:
            arr.append('Jinx')
    return arr

print "New Array: ", thisLengthArr(4,5)
print("\n")
