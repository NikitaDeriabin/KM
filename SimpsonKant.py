from FunctionKant import *
from math import *


class SimpsonKant():

    def __init__(self, a, b, n):
        self.h = (b - a) / n
        self.a = a
        self.b = b
        self.n = n
        #print(self.a, self.b, self.n, self.h)


    def getIForKant(self):
        interval = self.a
        fInPoints = FunctionKant.countFunc(self.b)
        for i in range(1, self.n):
            interval += self.h
            if (i % 2 == 1):
                fInPoints += 4 * FunctionKant.countFunc(interval)
            else:
                fInPoints += 2 * FunctionKant.countFunc(interval)

            #print('f(', interval, ') = ', fInPoints)
        return self.h / 3 * fInPoints