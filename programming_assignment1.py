#A1

print("Hello Python")
########################################

#A2

a=int(input())
b=int(input())
print(a+b,a//b)

#######################################

#A3

b = float(input())
h = float(input())
area = 0.5*b*h

print(area)
#######################################

#A4

a=5                      
b=3
c=b
b=a
a=c
print(a,b)

#OR

a=5
b=3
a=a+b
b=a-b
a=a-b

print(a,b)
#########################

#A5

import random
a=int(input())
b=int(input())
print(random.randint(a,b))
