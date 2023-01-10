#A1
def evenly_divisible(a,b,c):
    l = []
    for i in range(a,b+1):
        if (i%c == 0):
            l.append(i)
    return sum(l)

x,y,z = int(input())   
print(evenly_divisible(x,y,z))

#A2
def correct_signs(a):
    if a == True:
        return True
    else: 
        return False

print(correct_signs("13 > 44 > 33 > 1"))

#A3
def replace_vowels(a,b):
    x = "aeiou"
    for i in a:
        if i in x:
           a =  a.replace(i,b)
    return a

print(replace_vowels("the aardvark", "#"))

#A5
def hamming_distance(a,b):
    count = 0
    for i in a:
        for j in b:
          if (i == j):
            pass
        else:
            count+=1
    return count
print(hamming_distance("abcde", "bcdef"))