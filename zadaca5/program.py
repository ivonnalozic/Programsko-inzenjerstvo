Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Zadatak 5.3

import likovi
import funkcije

k1 = likovi.Kruznica(3)
k2 = likovi.Kvadrat(5)

print('*** test program ***')
print(k1, 'opsega', funkcije.opseg(k1), 'povrsine' , funkcije.povrsina(k1))
print(k2, 'opsega', funkcije.opseg(k2), 'povrsine', funkcije.povrsina(k2))
