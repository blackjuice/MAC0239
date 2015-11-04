import sys
import re
from numpy import matrix
import numpy as np

n = 4
k = 0
#n, k = [int(x) for x in input("Enter two numbers here: ").split()]
print (n)
print (k)
'''
matrix = [['A', 'B', 'C'], 
          ['D', 'E', 'F'], 
          ['G', 'H', 'I']]
'''
matrix = [['A', 'B', 'C', '1'],
           ['D', 'E', 'F', '2'],
           ['G', 'H', 'I', '3'],
           ['J', 'K', 'L', '4']]
#print (matrix)

print ("['A', 'B', 'C', '1']")
print ("['D', 'E', 'F', '2']")
print ("['G', 'H', 'I', '3']")
print ("['J', 'K', 'L', '4']")

# restricao linha
str = ""
for i in range (0, n):
    for j in range (0, n):
        for k in range (j + 1, n):
            strAux = "(" + "~" + matrix[i][j] + " | " + "~" + matrix[i][k] + ")"
            str = str + " & " + strAux

str = str[3:]
print (str)

# restricao coluna
str = ""
for i in range (0, n):
    for j in range (0, n):
        for k in range (j + 1, n):
            strAux = "(" + "~" + matrix[j][i] + " | " + "~" + matrix[k][i] + ")"
            str = str + " & " + strAux

str = str[3:]
print (str)

# restricao diagonal1
str = ""
for i in range (0, n - 1):
    #print ("manemapunomame1")
    for j in range (i, n - 1):
        for k in range(1, n - j):
            strAux = "(" + "~" + matrix[i][j] + " | " + "~" + matrix[i + k][j + k] + ")"
            str = str + " & " + strAux
    for j in range (0, i):
        for k in range(1, n - i):
            strAux = "(" + "~" + matrix[i][j] + " | " + "~" + matrix[i + k][j + k] + ")"
            str = str + " & " + strAux

str = str[3:]
print (str)

# restricao diagonal2
str = ""
for i in range (0, n):
    #print ("manemapunomame1")
    for j in range (0, n - i):
        for k in range(1, j + 1):
            strAux = "(" + "~" + matrix[i][j] + " | " + "~" + matrix[i + k][j - k] + ")"
            str = str + " & " + strAux
    for j in range (n - i, n):
        for k in range(1, n - i):
            strAux = "(" + "~" + matrix[i][j] + " | " + "~" + matrix[i + k][j - k] + ")"
            str = str + " & " + strAux

str = str[3:]
print (str)

# presenca linha
str = "("
for i in range (0, n):
    for j in range (0, n):
        strAux = matrix[i][j] + " | "
        str = str + strAux
    #print (strAux + "ohh")
    str = str[:-3]
    str =  str + ")" + " & " + "(" 

str = str[:-4]
print (str)
