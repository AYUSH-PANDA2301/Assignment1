#A1
def filter_list(l):
    a =[]
    for i in l:
        if type(i) == int:
            a.append(i)
    return a
print(filter_list([1, 2, "a", "b"]))

#A2
def reverse(a):
    return a[::-1]
print(reverse("Hello World"))

#A3
lst = [1, 2, 3, 4, 5, 6]
first,*middle,last = lst
print(first)
print(middle)
print(last)

#A5
def move_to_end(a,b):
    a = [i for i in a if i != b] + [j for j in a if j == b]
    return a
print(move_to_end([1, 3, 2, 4, 4, 1], 1))
