def dectobin(N):
    s = ""
    while (N != 0):
        if (N % 2 == 0):
            s = "0" + s
        else:
            s = "1" + s
 
            N -= 1
        N /= 2
    if (s == ""):
       s = "0"
    return s

x = int(input())
print(dectobin(x))
