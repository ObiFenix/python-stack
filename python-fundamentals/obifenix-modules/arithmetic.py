#=====================================
# OBIFENIX Modules: Computational Math
#=====================================

import math


class Underscore:
    def __init__ (self, list):
        self.list = list

    def map (self):
        for i self.list:
            print (i)

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

# AddingTwoNum = Arithmatic()
# print(AddingTwoNum.add(3,4))

map = Underscore([2,41,5,6,3])
map.map()
