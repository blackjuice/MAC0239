import sys
from numpy import matrix
import numpy as np

n = 3
k = 0
#n, k = [int(x) for x in input("Enter two numbers here: ").split()]
print (n)
print (k)

# Examples of how to create matrices
#   m1 = [ [1, 2, 3, 0], [4, 5, 6, 0], [7, 8, 9, 0] ]
#   print (m1)

r00 = 0
r01 = 0
r02 = 0
r03 = 0
r10 = 0
r11 = 0
r12 = 0
r13 = 0
r20 = 0
r21 = 0
r22 = 0
r23 = 0
r30 = 0
r31 = 0
r32 = 0
r33 = 0

R = np.matrix ([
    [r00, r01, r02, r03],
    [r10, r11, r12, r13],
    [r20, r21, r22, r23],
    [r30, r31, r32, r33]
])

print (R)

matrix = [['A', 'B', 'C'], 
          ['D', 'E', 'F'], 
          ['G', 'H', 'I']]

print (matrix)

for x in range (0, n):
    for i in range (0, n):
        for j in range (i + 1, n):
            print ("matrix[", x, "][", i, "]", "-> matrix[", x, "][", j, "]")
