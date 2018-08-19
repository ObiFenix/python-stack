#=====================================
# OBIFENIX Modules: Computational Math
#=====================================

import math

# List operator of increments of (2 * list values)
# ================================================
class Underscore:

    def map ( self, list, function ):
        for i in range( len(list) ):
            list[i] = function ( list[i] )
        return list

    def reduce ( self, list, function ):  # Reduced all elements in a list by the min. within the list
        last = len(list)
        for index in range( last ):
            next = index+1
            if ( next < last ):
                list[next] = function ( list[index], list[next] )
        return list

    def findId ( self, list, function ):
        print ("... Searching for 1st matching ID > 4")
        for i in range ( len(list) ):
            if ( function(list[i]) ):
                return list[i]
        return self

    def matchId ( self, target, list, function ):
        idNotfound = False
        print ("... Trying to match ID {}".format( target) )
        for i in range ( len(list) ):
            if ( function ( int(target), list[i]) ):
                idNotfound = True
        print ("... ID match found") if (idNotfound) else print ("... Sorry! No ID match found")
        return self

    def filter ( self, list, function ):
        count = 0
        for item in range( len( list )):
            if ( function( list[item] )):
                count += 1
                list[count], list[item] = list[item], list[count]
        # list = list[:count]
        print (f"Return: List of all <Even> ID's: {list}")
        return self

    def reject ( self, list, function ):
        count = 0
        for item in range( len( list )):
            if ( function( list[item] )):
                count += 1
                list[count], list[item] = list[item], list[count]
        # list = list[:count]
        print (f"Return: List of all  <Odd> ID's: {list}")

    def filter_btw_minmax ( self, list, min, max, function ):  # Filter out any items btw min and max (INCLUSIVE)
        count = 0
        last = -1#len(list)
        for current in range ( len (list)):
            # print(list[current])
            if ( list[current] < min or list[current] > max ):
                # list[current], list[last] = list[last], list[current]
                # print("before modifying last item: ",last)
                last += 1
                # print(" after modifying last item: ", last)
                list[current] = list[last]
            else:
                # print (count, current)
                count += 1

        # print (count)
        list = list[:count]
        list.sort()
        return list


# Arithmetics
# ===========
class Arithmatic:
    def add(self, x, y):       return x + y
    def subs(self, x, y):      return x - y
    def mult(self, x, y):      return x - y
    def divFloat(self, x, y):  return x / y
    def divInt(self, x, y):    return x // y
    def square(self, x):       return x * x
    def sqrt(self, x):         return math.sqrt(x)
    def ceil(self, x):         return math.ceil(x)
    def floor(self, x):        return math.floor(x)
    def mod(self, x, y):       return math.fmod(x, y)
    def nRoot(self, co, ex):   return math.pow(co, ex)
    def power(self, co, ex):   return math.pow(co, ex)
    def log2(self, x):         return math.log(x)
    def log10(self, x):        return math.log(x)
    def ln(self, x):           return math.log1p(x)
    def logx(self, x, base):   return math.log(x,base)
    def exp(self, e=1):        return math.exp(e)

    # => Booleans testing approximate equality
    def isFinite(self, num):   return math.isfinite(num)    # TRUE if Finite number and FALSE if not
    def isInfinity(self, num): return math.isinf(num)       # TRUE if Infinit number and  FALSE if not
    def isNan(self, num):      return math.isnan(num)       # TRUE if NaN and FALSE if a num is a number


if __name__ == "__main__":
    # Testing Several Instances of the class <Objects>
    # ================================================
    # AddingTwoNum = Arithmatic()
    myL = [2,4,6,3,9,5,1,8,7]
    _ = Underscore()
    _.map(myL, lambda num: num+(2*num))
    _.reduce(myL, lambda num1,num2: num1-num2)
    _.filter_btw_minmax(myL, 3, 6, None)        # lambda num: num


    # Filtering list by getting rid of unrequested elements
    # -----------------------------------------------------
    myL = [1,2,3,4,5,6]
    print ("\n Given: List of available ID's:", myL)
    # print (f"List of all <Even> ID's: {_.findId( myL, lambda id: id > 4)}")
    _.filter(myL, lambda x: x%2==0)   # should return [2,4,6]
    _.reject(myL, lambda x: x%2==0)   # should return [1,3,5]

    # Mapping...
    # -------
    # myL = [1,2,3,4,5,6]
    # print ("\n Given: List of available ID's:", myL)
    # print( map.map() )
    # print ("Before: ", myL)
    # print (" After: ", reduce.reduce() )

    # filter i-btw items given min & max
    # ----------------------------------
    # myL = [1,2,3,4,5,6]
    # print ("\n Given: List of available ID's:", myL)
    # print ("Before: ", myL)
    # print (" After: ", filter.filter_btw_minmax(3, 6) )

    # Find target ID's > 4
    # --------------------
    # print ()
    # print ("List of available ID's:", myL)
    # print ("1st matching ID#: %d" % _.findId( myL, lambda id: id > 4))
    #

    # Find target ID match
    # --------------------
    # myL = [1,2,3,4,5,6]
    # print ("\n Given: List of available ID's:", myL)
    # print ("List of available ID's:", myL)
    # myItem = input("::> Enter ID#: ")
    # _.matchId(myL, myItem, lambda id1, id2: id1 == id2)
