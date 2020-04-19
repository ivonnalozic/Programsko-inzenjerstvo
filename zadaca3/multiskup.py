Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Zadatak 3.1
class MultiSkup(object):

      def __init__(self, rjecnik = None):
            self.__rjecnik = {}
            self.__elementi = []

            if rjecnik is not None:
                  self.__rjecnik = rjecnik
                  for i in self.__rjecnik:
                    if i not in self.__elementi:
                        self.__elementi.append(i)



      def __str__(self):
        string = []
        for key in self.__elementi:
            string.append("%r*%r" % (key,self.__rjecnik.count(key)))
        return "{{ %s }}" % ", " .join(string)

#Zadatak 3.2

      def __iter__(self):
         return iter(self.__rjecnik)

      def __repr__(self):
        string = []
        for key in self.__elementi:
            string.append("%r*%r" % (key,self.__rjecnik.count(key)))
        return "Multiskup(" + repr(self.__rjecnik)+ ")"


#Zadatak 3.3

      def add(self, broj , times=1):
         for i in range(times):
            self.__rjecnik.append(broj)

      def remove(self, broj , times=1):
         for i in range(times):
            self.__rjecnik.remove(broj)



print('*** test 1 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
print(a)

print('*** test 2 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
for el in a:
 print(el)
print(repr(a))

print('*** test 3 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
a.add(4)
print(a)
a.add(2,3)
print(a)
a.remove(4,2)
print(a)
