#A1
n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a)
print(sum(a))
##########################
#A2
n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a)
print(max(a))

#################################
#A3
n = int(input("enter limit"))
a = list()
for i in range(0,n):
    x = int(input())
    a.append(x)
print(a[::-1])
###############################3
#A4
n = int(input('enter limit for first half'))
n1 = int(input('enter limit'))
a = list()
for i in range(0,n1):
    x = int(input())
    a.append(x)

print("first half of array :",a[:n])
b = a[:n]
print(a[n:]+b)
#####################################
#A5
