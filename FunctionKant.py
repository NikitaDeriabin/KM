from math import *
class FunctionKant:

    def countFunc(x):
        return 1/(sqrt(x) * (pow(e, (x/2)) + 3)) - 1/4 * pow(x, -1/2) + 1/32 * pow(x, 1/2) + 1/256 * pow(x, 1.5) \
               - 1/614 * pow(x, 2.5) - 5/49152 * pow(x, 3.5)
