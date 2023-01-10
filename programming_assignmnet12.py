#A2
dict = {"key1": 1, "key2": 2}
l = []
for i in dict.values():
    l.append(i)
print(sum(l))

#A2
a = {}
b = {}
n = int(input())
for i in range(n):
    k = input()
    v = input()
    a.update({k:v})

for j in range(n):
    x = input()
    y = input()
    b.update({x:y})
    
print(a.update(b))

#A1:
a={'key1': 1,"key2":2,'key3': 1}
l = []
for i in a.values():
    l.append(i)

for j in l:
    if l.count(j) == 1:
        print(j)

#A4
b = {'name': ['ayush','sam','ram'], 'age':[21,22,23]}

a = dict(zip(b['name'],b['age']))
print(a)

#A6
from collections import OrderedDict
dict = OrderedDict.fromkeys(input())
pattern = input()
plen = 0

for i,j in dict.items():
    if (i == pattern[plen]):
        plen += 1

    if (plen == len(pattern)):
        print ('correct order')
else:
    print('wrong order')

#A7

a = {'a': 1, 'c': 2, 'b':3}
l = []
for i in a.keys():
    l.append(i)

l.sort()

a_dict = {j:a[j] for j in l}
print(a_dict)
#or
a = {'a': 1, 'c': 2, 'b':3}
b = sorted(a.items())
print(b)
