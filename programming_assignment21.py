#A1
def next_in_line(a,b):
    if len(a) !=0:
        a.append(b)
        return a[1:]
    else:
        print("no list has been selected")
    
print(next_in_line([7, 6, 3, 23, 17], 10))

#A2
def get_budgets(a):
    l = []
    for i in a:
        for j in i:
            if j == 'budget':
             l.append(i[j])
    return sum(l)

print(get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]) 
)

#A3
def alphabet_soup(a):
    return ''.join(sorted(a))

print(alphabet_soup("hello"))

#or

def alphabet_soup(a):
    l = []
    for i in range(len(a)):
        l.append(a[i])
    for i in range(len(a)):
        for j in range(len(a)):
            if l[i]<l[j]:
                l[i],l[j] = l[j],l[i]
    b = ""
    for i in range(len(a)):
        b = b+l[i]
    return b

print(alphabet_soup("hello"))



