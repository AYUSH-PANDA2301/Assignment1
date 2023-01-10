#A1
import math
c = 50
h = 30

a = input()
d = a.split(',')
print(d)

l = []
for i in d:
    q = math.sqrt((2*c*int(i))//h)
    l.append(int(q))

print(l)

#A2
x = int(input('enter number of rows: '))
y = int(input('enter number of columns: '))

m = [[i*j for i in range(y)]for j in range(x)]
print(m)

for i in range(x):
    for j in range(y):
        print(m[i][j],end = " ")
    
#A3

a = input()
d = a.split(',')
d.sort()
print(d)
#A4
a = input()
l = a.split()
for i in l:
    if l.count(i)>1:
        l.remove(i)
l.sort()

for j in l:
  print(j,end = " ")

#A5
a = input()
digit = 0
letter = 0
for i in a:
    if i.isdigit():
        digit += 1
    elif i.isalpha():
        letter += 1
    else:
        pass
print(f"digit:{digit} , letter: {letter}")

#A6

password = input()
small = 'abcdefghijklmnopqrstuvwxyz'
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
sp_char = '$#@'




