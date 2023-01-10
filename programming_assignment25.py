#A1
def equal(a,b,c):
    count = 0
    if a == b or a==c:
        count+=1
    if b==a or b == c:
        count+=1
    if c==a or c==b:
        count+=1
    return count
print(equal(3,4,3))
print(equal(1,1,1))
print(equal(3,4,1))

#A2
def dict_to_list(a):
     l = [(k,v) for k,v in a.items()]
     l.sort()
     return l
print(dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
})
)

#A3
def mapping(a):
    b = {i:i.upper() for i in a}
    return b
print(mapping(["p", "s"]) )

#A5
def ascii_capitalize(a):
    b = ""
    for i in range(len(a)):
        if (ord(a[i])%2 == 0):
            b = b + a[i].upper()
        else:
             b = b + a[i].lower()
    return b 
print(ascii_capitalize("THE LITTLE MERMAID"))