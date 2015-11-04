import sys
from numpy import matrix
import numpy as np

n = 3
k = 0
#n, k = [int(x) for x in input("Enter two numbers here: ").split()]
print (n)
print (k)

matrix = [['A', 'B', 'C'], 
          ['D', 'E', 'F'], 
          ['G', 'H', 'I']]

# print (matrix)

str = ""
for x in range (0, n):
    for i in range (0, n):
        for j in range (i + 1, n):
            strAux = "(" + matrix[x][i] + " | " + matrix[x][j] + ")"
            str = str + " & " + strAux

str = str[3:]
print (str)


