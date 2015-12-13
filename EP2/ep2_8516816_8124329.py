'''
  integrantes:
    Leonardo Daneu Lopes (8516816)
    Lucas Sung Jun Hong  (8124329)

'''

#from parser import CTLtree
#CTLtree = CTLtree()
#return CTLtree.run()
from parser import CTLtree
#from subprocess import call
from pyeda.inter import *
import os

#------------main--------------

'''
# Test
# ....
#   The formula
#   f-> = ( ~a & ~b & ~c & ~d ) | ( ~a & ~b & c & ~d ) | ( a & ~b & ~c & d ) | ( ~a & b & ~c & ~d )
#   produces the page 386 pdf truth table

a, b, c = map(bddvar, 'abc')
f = ( a & b & ~c ) | ( ~a & b & c ) | ( ~a & ~b & c )
print ( list(f.satisfy_all()) )
'''

numeroEstados = input()
kripke = input()
rotulos = input()
formulaCTL = str( CTLtree( input() ) ) #formulaCTL = input(); formulaCTL = str( CTLtree(formulaCTL) )
interest = input()
#print (numeroEstados, kripke, rotulos, formulaCTL, interest)
#numeroEstados = int(numeroEstados) + 3
#print (numeroEstados)
#x1, x2, x3 = map(bddvar, 'x1x2x3')
#X = exprvars('x', 3)


'''# Testing X array

X = bddvars('x', 3, 1)
Y = str(X)
#print (Y)
f = ( X[0,0] & X[1,0] & ~X[2,0] ) | ( ~X[0,0] & X[1,0] & X[2,0] ) | ( ~X[0,0] & ~X[1,0] & X[2,0] )
#print ( list(f.satisfy_all()) )

a, b, c = map(bddvar, 'abc')
f1 = ( a & b & ~c ) | ( ~a & b & c ) | ( ~a & ~b & c )
#print ( list(f1.satisfy_all()) )

'''



'''
#f = ( x[0] & x[1] & ~x[2] ) | ( ~x[0] & x[1] & x[2] ) | ( ~x[0] & ~x[1] & x[2] )
#print ( list(f.satisfy_all()) )

n = 3
X = exprvars("x", n, n)

# Row constraint
R = And(*[OneHot(*[X[r,c] for c in range(n)]) for r in range(n)])

# Column constraint
C = And(*[OneHot(*[X[r,c] for r in range(n)]) for c in range(n)])

R = expr2bdd(R)
print (R.satisfy_all)
#print (C)
'''

'''


# Assuming X = s2 = ~x1 * ~x2 * x3
a, b, c = map(bddvar, 'abc') # abc exists
Bx_prime = ( ~a ) #Bx_prime = ( ~a & ~b & c )
d, e, f = map(bddvar, 'def')
Bx_prime_test = ( d ) #Bx_prime_test = ( ~c & ~d & f )
#Bx_prime_test = ( ~d & ~e & f )

New = (Bx_prime) | (Bx_prime_test)
print (New)
print ( New.satisfy_all )
print (New.satisfy_one())



'''
# Testing simple expr:
f1 = expr("( ~a & ~b & c )")
#print(f1)
f2 = expr("( ~d )")
f3 = f1 | f2
f3 = expr2bdd(f3)
#print (f3)
#print (f3.satisfy_one)
#print (f3.satisfy_all)
#print (isinstance(f3, BinaryDecisionDiagram))

a, b, c, d = map(bddvar, 'abcd') # abc exists
f3 = ( ~a & ~b & c ) | ( ~d )
#print (f3.satisfy_one)

'''
n = 3
X = bddvars("x", 3)
Y = bddvars("y", 3)
    Xconta = And(( [X[c] for c in range(n) ]))
    Yconta = And(( [Y[c] for c in range(n) ]))
    Zconta = Or(Xconta, Yconta)
    #   Zconta = Xconta | Yconta   :isso nao roda
    print (Zconta.satisfy_one())

=> {}
'''

'''
n = 3
X = bddvars("x", 3)
Y = bddvars("y", 3)
    Xconta = X[0] & X[1] & X[2]
    Yconta = Y[0] & Y[1] & Y[2]
    #   Zconta = Or(Xconta, Yconta)  :sai estranho
    Zconta = Xconta | Yconta
    print (Zconta.satisfy_one())
    print ( list(Zconta.satisfy_all()) )    # **HERE IT IS HOW PRINT ALL**
=> {y[0]: 1, y[2]: 1, y[1]: 1, x[0]: 0}
'''
n = 3
X = bddvars("x", 3)
Y = bddvars("y", 3)
Xconta = X[0] & X[1] & X[2]
Yconta = Y[0] & Y[1] & Y[2]
#   Zconta = Or(Xconta, Yconta)  :sai estranho
Zconta = Xconta | Yconta
print ( list(Zconta.satisfy_all()) )
