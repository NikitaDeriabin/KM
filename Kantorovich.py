from math import *
from SimpsonKant import *

class Kantorovich():

    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
        self.I1 = 0
        self.I2 = 0

    def getI1(self):
        self.I1 = 1/2 * pow(self.b, 0.5) - 1/48 * pow(self.b, 1.5) - 1/640 * pow(self.b, 2.5) + 1/2149 * pow(self.b, 3.5)\
             + 5/221184 * pow(self.b, 4.5)
        return self.I1

    def getI2(self):
        simpson = SimpsonKant(self.a, self.b, self.n)
        return simpson.getIForKant()
