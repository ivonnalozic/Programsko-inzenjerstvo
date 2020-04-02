Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Zadatak 2.1

class Stvar(object):

    broj_stvari = 0

    def __init__(self):
        Stvar.broj_stvari += 1


    def __del__(self):
        Stvar.broj_stvari -= 1


print('*** test 1***')
s1 = Stvar()
s2 = Stvar ()
s3 = s2
print(Stvar.broj_stvari)
del(s2)
print(Stvar.broj_stvari)
del(s3)
print(Stvar.broj_stvari)
del(s1)
print(Stvar.broj_stvari)
