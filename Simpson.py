from Function import *
from math import *


class Simpson():
    def __init__(self, a, b, n):
        self.h = (b - a) / n
        self.a = a
        self.b = b
        self.n = n
        #print(self.a, self.b, self.n, self.h)

    def getI(self):
        interval = self.a
        fInPoints = Function.countFunc(pi/2) + Function.countFunc(pi)
        for i in range(1, self.n):
            interval += self.h
            if(i % 2 == 1):
                fInPoints += 4 * Function.countFunc(interval)
            else:
                fInPoints += 2 * Function.countFunc(interval)

            #print('f(', interval, ') = ', fInPoints)
        return self.h / 3 * fInPoints


