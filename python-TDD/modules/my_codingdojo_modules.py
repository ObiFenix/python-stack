#=====================================
# OBIFENIX Modules: Computational Math
#=====================================

import math

# List operator of increments of (2 * list values)
# ================================================
class Underscore:
    def __init__ (self, list, function):
        self.list = list
        self.func = function if (function) else None

    def map (self):
        for i in range(len(self.list)):
            self.list[i] = self.func(self.list[i])
        return self.list

    def reduce (self):  # Reduced all elements in a list by the min. within the list
        last = len(self.list)
        for index in range(last):
            next = index+1
            if (next < last):
                self.list[next] = self.func(self.list[index], self.list[next])
        return self.list

    def find (self, target):
        idNotfound = False
        print ("... Trying to match ID {}".format(target))
        for i in range (len(self.list)):
            if (self.func(int(target), self.list[i])):
                idNotfound = True
        print ("... ID match found") if (idNotfound) else print ("... Sorry! No ID match found")
        return self

    def filter_btw_minmax (self, min, max):  # Filter out any items btw min and max (INCLUSIVE)
        left  = 0
        count = 0
        right = -1#len(self.list)
        # _nth  = len(self.list)
        for index in range(len(self.list)):
            # print(self.list[index])
            if (self.list[index] < min or self.list[index] > max):
                # self.list[index], self.list[right] = self.list[right], self.list[index]
                print("before right: ",right)
                right += 1
                print(" after right: ", right)
                self.list[index] = self.list[right]
            else:
                print (count, index)
                count += 1

        print (count)
        self.list = self.list[:count]
        self.list.sort()
        return self.list

    # def reject (self):
        # your code



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
    map = Underscore(myL, lambda num: num+(2*num))
    reduce = Underscore(myL, lambda num1,num2: num1-num2)
    filter = Underscore(myL, None) # lambda num: num
    findMe = Underscore(myL, lambda item1, item2: item1 == item2) # Return a Boolean (T or F)

    # print( map.map() )
    # print ("Before: ", myL)
    # print (" After: ", reduce.reduce() )

    # print ()
    # print ("Before: ", myL)
    # print (" After: ", filter.filter_btw_minmax(3, 6) )

    print ()
    print ("List of available ID's:", myL)
    myItem = input("::> Enter ID#: ")
    findMe.find(myItem)
