from LeftRectangle import *
from Kantorovich import *
from Simpson import *


if __name__ == '__main__':
    lRect = LeftRectangle(pi/2, pi, 30)
    lRect2 = LeftRectangle(pi/2, pi, 60)
    print('Інтеграл методом лівих прямокутників 2h: {0}' .format(lRect.getI()) )
    print('Інтеграл методом лівих прямокутників h: {0}' .format(lRect2.getI()) )
    print('Похибка за Рунге-Ромбергом:', abs(lRect.getI() - lRect2.getI()))
    print()

    simpson = Simpson(pi/2, pi, 20)
    simpson2 = Simpson(pi/2, pi, 40)
    print('Інтеграл методом Сімсона 2h: {0}' .format(simpson.getI()))
    print('Інтеграл методом Сімсона h: {0}' .format(simpson2.getI()))
    print('Похибка за Рунге-Ромбергом:', abs(simpson.getI() - simpson2.getI()))
    print()

    kant = Kantorovich(0, 2, 20)
    print('Інтеграл методом Канторовича: {0}' .format(kant.getI1() + kant.getI2()))

