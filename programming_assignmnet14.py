#A1
class gener:
    def __init__(self):
        pass
    def div_7(self,x):
        for i in range(x):
            if (i%7 == 0):
                print(i)
      
n = int(input())
a = gener()
a.div_7(n)

#A2
import collections
a = input()
b = a.split()
b.sort()
c = {}
for item,count in collections.Counter(b).items():
    c.update({item:count})
print(c)

#A3
class person:
    def getgender(self):
        pass
class male(person):
    def getgender(self):
        return "male"
class female(person):
    def getgender(self):
        return "female"

a = male()
b = female()
print(a.getgender())
print(b.getgender())

#A4
import gzip
s = "hello world!hello world!hello world!hello world!"
s.compress(s)

print(s)


