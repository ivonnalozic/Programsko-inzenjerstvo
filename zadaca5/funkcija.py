Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Zadatak 5.2

import likovi
from math import pi , pow

def opseg(lik):
    if isinstance(lik,likovi.Kruznica):
        return lik.radijus * 2 * pi
    elif isinstance(lik,likovi.Kvadrat):
        return lik.stranica * 4


def povrsina(lik):
    if isinstance(lik,likovi.Kruznica):
        return pow(lik.radijus,2) * pi
    elif isinstance(lik,likovi.Kvadrat):
        return lik.stranica * lik.stranica

if __name__ == '__main__':
    print('*** test funkcije ***')
    print(opseg.__name__)
    print(povrsina.__name__)
