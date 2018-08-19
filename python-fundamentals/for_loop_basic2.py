#                         [ For Loop Basic II ] 

# Objectives
# =============================================================
# <> Write functions only using basic building blocks of Python
# <> Utilize for loops, functions, lists, and other data types
# =============================================================


# Function 1: Biggie Size 
# -----------------------
# => Shall take in an array
# => Shall changes all positive numbers in the array to "big". 
#    Ex: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].
def makeItBig( arr ):
    for k in range(len(arr)):
        if (arr[k] > 0):
            arr[k] = 'big'
    print ("\n Function #1 outputs: ",arr)   # Print arr for testing:

makeItBig([-1, 3, 5, -2])



# Function 2: Count Positives
# ---------------------------
# => Shall take in an array of numbers
# => Shall replace last value with number of positive values. 
#    Ex: countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.
def countPositives( arr ):
    lastSum = 0
    for k in range(len(arr)):
        if arr[k] > 0:
            lastSum += 1
            #lastSum += arr[k]
    arr[-1] = lastSum
    return arr

print ("\n Function #2 outputs: ", countPositives([-1,1,1,1]))



# Function 3: SumTotal
# --------------------
# => Shall take in an array as an argument
# => Shall return the sum of all the values in the array.
#    Ex: sumTotal([1,2,3,4]) should return 10
def sumTotal( arr ):
    sum=0
    for k in arr:
        sum += k
    return sum

print ("\n Function #3 outputs: The sum of all elements in ", [1,2,3,4], 'is equal to ', sumTotal([1,2,3,4]))



# Function 4: Average
# -------------------
# => Shall take in array as an argument
# => Shall return the average of all the values in the array.
#    Ex: average([1,2,3,4]) should return 2.5
def average( arr ):
    sum=0
    for k in arr:
        sum += k
    return sum/len(arr)

print ("\n Function #4 outputs: The average of all elements in ", [1,2,3,4], 'is equal to ', average([1,2,3,4]))



# Function 5: Length
# ------------------
# => Shall take in an array as an argument
# => Shall return the length of the array.
#    Ex: length([1,2,3,4]) should return 4
def length( arr ):
    return len(arr)

print ("\n Function #5 outputs: The Length of array ", [1,2,3,4], "= ", length([1,2,3,4]))



# Function 6: Minimum
# -------------------
# => Shall take in an array as an argument
# => Shall return the minimum value in the array.  
# => Shall return false if the passed array is empty,
#    Ex: minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minimum( arr ):
    min=arr[0]
    for k in arr:
        if min > k:
            min = k
    return min

print ("\n Function #6 outputs: The minimum value in array ", [-1,-2,-3,4], "is equal to ", minimum([-1,-2,-3,4]))



# Function 7: Maximum
# -------------------
# => Shall take in an array as an argument 
# => Shall return the maximum value in the array.
# => Shall return false if the passed array is empty,
#    Ex: maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -3.
def maximum( arr ):
    max=arr[0]
    for k in arr:
        if max < k:
            max = k
    return max

print ("\n Function #7 outputs: The maximum value in array ", [-1,-2,-3,4], "is equal to ", maximum([-1,-2,-3,4]))



# Function 8: UltimateAnalyze
# ---------------------------
# => Shall take an array as an argument
# => Shall return a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
def ultimateAnalyze( arr ):
    return { 
      'sum': sumTotal(arr),
      'avg': round(sumTotal(arr)/len(arr),2), 
      'min': minimum(arr),
      'max': maximum(arr), 
      'length': len(arr)
    }

data = ultimateAnalyze([-1,-2,4,2,6,-5])
print ("\n Function #8 outputs: From array", [-1,-2,4,2,6,-5], ":")
for info in data:
    if (info == 'min'):
        print ("\t\t      => Minimum  value in array: ", data['min'])
    elif (info == 'max'):
        print ("\t\t      => Maximum  value in array: ", data['max'])
    elif (info == 'sum'):
        print ("\t\t      => sumTotal value in array: ", data['sum'])
    elif (info == 'avg'):
        print ("\t\t      => Average  value of array: ", data['avg'])
    elif (info == 'length'):
        print ("\t\t      => The Length of the array: ", data['length'])



# Function 9: ReverseList
# -----------------------
# => Shall take an array as an argument
# => Shall return an array in a reversed order.
def reverseList( arr ):
    # Base case
    if len(arr) < 1:
        return

    left = 0
    right = len(arr)-1

    while (left < right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right]= temp
        left += 1
        right -= 1
    return arr

print("\n Function #9 outputs: The reverse order of array ",[3,1,7,0,4,6,2,5,9])
print("\t\t\t\t\t\t ",reverseList([3,1,7,0,4,6,2,5,9]),"\n")
