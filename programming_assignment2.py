#A3
import calendar

y = int(input("enter year: "))
m = int(input("enter month: "))

print(calendar.month(y,m))
######################################

#A5

a=5
b=3
a=a+b
b=a-b
a=a-b

print(a,b)

################################

#A4
import cmath
#format: ax^2+bx+c
a = int(input())
b = int(input())
c = int(input())

D = b**2 - 4*a*c

print("root 1:" (-b+cmath.sqrt(D))//2 ,"root 2:" (-b-cmath.sqrt(D))//2)
###############################################

#A1

a = float(input("enter distance in Km: "))
kilo_to_mile = a*0.621
print(kilo_to_mile)

####################################

#A2
a = float(input("enter temperature in celcius : "))
cel_to_faren = a*9//5 + 32
print(cel_to_faren)