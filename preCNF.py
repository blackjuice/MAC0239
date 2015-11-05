import sys

import re

from numpy import matrix

import numpy as np



from pyeda.inter import *



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

restRow = ""

for i in range (0, n):

    for j in range (0, n):

        for k in range (j + 1, n):

            restRowAux = "(" + "~" + matrix[i][j] + " | " + "~" + matrix[i][k] + ")"

            restRow = restRow + " & " + restRowAux



restRow = restRow[3:]

print (restRow)



# restricao coluna

restColumn = ""

for i in range (0, n):

    for j in range (0, n):

        for k in range (j + 1, n):

            restColumnAux = "(" + "~" + matrix[j][i] + " | " + "~" + matrix[k][i] + ")"

            restColumn = restColumn + " & " + restColumnAux



restColumn = restColumn[3:]

print (restColumn)



# restricao diagonal1

restDiag1 = ""

for i in range (0, n - 1):

    #print ("manemapunomame1")

    for j in range (i, n - 1):

        for k in range(1, n - j):

            restDiag1Aux = "(" + "~" + matrix[i][j] + " | " + "~" + matrix[i + k][j + k] + ")"

            restDiag1 = restDiag1 + " & " + restDiag1Aux

    for j in range (0, i):

        for k in range(1, n - i):

            restDiag1Aux = "(" + "~" + matrix[i][j] + " | " + "~" + matrix[i + k][j + k] + ")"

            restDiag1 = restDiag1 + " & " + restDiag1Aux



restDiag1 = restDiag1[3:]

print (restDiag1)



# restricao diagonal2

restDiag2 = ""

for i in range (0, n):

    #print ("manemapunomame1")

    for j in range (0, n - i):

        for k in range(1, j + 1):

            restDiag2Aux = "(" + "~" + matrix[i][j] + " | " + "~" + matrix[i + k][j - k] + ")"

            restDiag2 = restDiag2 + " & " + restDiag2Aux

    for j in range (n - i, n):

        for k in range(1, n - i):

            restDiag2Aux = "(" + "~" + matrix[i][j] + " | " + "~" + matrix[i + k][j - k] + ")"

            restDiag2 = restDiag2 + " & " + restDiag2Aux



restDiag2 = restDiag2[3:]

print (restDiag2)



# presenca linha

presencaLinha = "("

for i in range (0, n):

    for j in range (0, n):

        presencaLinhaAux = matrix[i][j] + " | "

        presencaLinha = presencaLinha + presencaLinhaAux

    #print (presencaLinhaAux + "ohh")

    presencaLinha = presencaLinha[:-3]

    presencaLinha =  presencaLinha + ")" + " & " + "(" 



presencaLinha = presencaLinha[:-4]

print (presencaLinha)





print ()

formula = presencaLinha + " & " + restRow + " & " + restColumn + " & " + restDiag1 + " & " + restDiag2

print (formula)
