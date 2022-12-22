#A1
n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a)
print(sum(a))
####################################
#A2
n = int(input("enter limit"))
a = list()
mul=1
for i in range(0,n):
    x = int(input())
    a.append(x)
for j in a:
    mul = mul*j
print(mul)
####################################
#A3

n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a)
print(min(a))

######################################
#A4
n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a)
print(max(a))
######################################
#A5

n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a)
a.sort()
print(a[-2])
###############################
#A6
N=int(input('enter N'))
n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a)
a.sort()
print(a[-N])
#################################
#A7
n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a)

for i in a:
    if i%2 ==0:
        print(i)
#############################
#A8
n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a)

for i in a:
    if i%2 !=0:
        print(i)
#############################
#A9
l =[1,2,3,[],4,5]
for i in l:
    if i == []:
        l.remove(i)
print(l)
#######################
#A11
import collections
n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a)

for item,count in collections.Counter(a).items():
    print(item,'-',count)
#####################################
#A10
n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a)

b = a[:]
print(b)