#A1
r = int(input('enter number of rows : '))
c = int(input('enter number of columns : '))

print('enter elements for matrix 1')
matrix1 = [[int(input()) for i in range(c)]for j in range(r)]
print('enter elements for matrix 2')
matrix2 = [[int(input()) for i in range(c)]for j in range(r)]

result = [[0 for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        result[i][j]=matrix1[i][j]+matrix2[i][j]

for i in range(r):
    for j in range(c):
        print(result[i][j],end = ' ')
    print('\n')
############################################
#A2
r = int(input('enter number of rows : '))
c = int(input('enter number of columns : '))
n = int(input())

print('enter elements for matrix 1')
matrix1 = [[int(input()) for i in range(n)]for j in range(r)]
print('enter elements for matrix 2')
matrix2 = [[int(input()) for i in range(c)]for j in range(n)]

result = [[0 for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        for k in range(n):
         result[i][j]=result[i][j]+matrix1[i][k]*matrix2[k][j]

for i in range(r):
    for j in range(c):
        print(result[i][j],end = ' ')
    print('\n')
#################################################
#A3
r = int(input('enter number of rows : '))
c = int(input('enter number of columns : '))

print('enter elements for matrix 1')
matrix1 = [[int(input()) for i in range(c)]for j in range(r)]

print('matrix1 : ')
for i in range(r):
    for j in range(c):
        print(matrix1[i][j],end = ' ')
    print('\n')

result = [[0 for i in range(c)] for j in range(r)]

for i in range(r):
    for j in range(c):
        result[i][j] = matrix1[j][i]
print('result : ')
for i in range(r):
    for j in range(c):
        print(result[i][j],end = ' ')
    print('\n')
############################################
#A5

a= input()
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

for i in a:
    if i in punc:
        a = a.replace(i, "")
 
print(a)