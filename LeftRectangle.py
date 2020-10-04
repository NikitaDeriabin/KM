from Function import *
from math import *


class LeftRectangle:
    def __init__(self, a, b, n):
        self.h = (b - a) / n
        self.a = a
        self.b = b
        self.n = n
        #print(self.a, self.b, self.n, self.h)

    def getI(self):
        fInPoints = 0
        interval = self.a
        for i in range(self.n):
            fInPoints += Function.countFunc(interval)
            #print('f(', interval, ') = ', fInPoints)
            interval += self.h

        return self.h * fInPoints
