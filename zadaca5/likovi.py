Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Zadatak 5.1
class Kruznica(object):

    def __init__(self,radijus):
        self.radijus = radijus

    def __str__(self):
        return "Kruznica radijusa %.2f" % (self.radijus)

class Kvadrat(object):

    def __init__(self,stranica):
        self.stranica = stranica

    def __str__(self):
        return "Kvadrat stranice %.2f" %(self.stranica)


if __name__ == '__main__':
    print('*** test likovi ***')
    kruznica = Kruznica(3)
    kvadrat = Kvadrat(4.5)
    print(kruznica)
    print(kvadrat)
