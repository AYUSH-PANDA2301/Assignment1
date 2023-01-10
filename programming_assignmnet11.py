#A2
i = int(input('enter i: '))
a = input('enter a string: ')
print(a[:i]+a[i+1:])

#A1
k = int(input())
a = input()
b = []
c = a.split()
for i in c:
    if len(i)>k:
        b.append(i)
print(b)

#A7

a= input()
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
count = 0

for i in range(len(a)):
    if a[i] in punc:
       count+=1
    
if count>=1:
    print("string contains special characters")
else:
    print('no special characters')

#A6

a = input() 
count = 1

for i in range(len(a)):
   
    for j in range(i+1,len(a)):
        if a[i] == a[j]:
            count+=1

if count>1:
    print(a[i])
#or

import collections

a = input()

for item,count in collections.Counter(a).items():
    if count>1:
        print(item)

#A5

a = input()
b = input()
la = a.slpit()
lb = b.split()
uncommon = ""
for i in la:
    if i not in lb:
        uncommon+=i

for j in lb:
    if j not in la:
        uncommon+=j


print(uncommon)
#A4

a = input()
bin = '01'
x = False
for i in a:
    if i not in bin:
        x = True

if x :
    print('no')
else:
    print('yes')

#A3

