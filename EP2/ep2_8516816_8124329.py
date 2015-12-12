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

print ("printing")

#n = input()
#print (n)
#print (str(CTLtree("AG+(x1)(-x2)")))
#print ( CTLtree.test() )
#CTLtree.run()
#s = CTLtree("")
#s.test()
#X = ttvars('x', 4)
#print (X)
#f1 = expr("~x[1] & ~x[2] & ~x[1] & ~x[2] | ~x[1] & ~x[2] & x[1] & ~x[2] | x[1] & ~x[2] & ~x[1] & x[2] | ~x[1] & x[2] & ~x[1] & ~x[2] ")
#f1 = ~x[1] & ~x[2] & ~x[1] & ~x[2] | ~x[1] & ~x[2] & x[1] & ~x[2] | x[1] & ~x[2] & ~x[1] & x[2] | ~x[1] & x[2] & ~x[1] & ~x[2]
#f1m = espresso_tts(f1)
#print (f1m)
#print (f1.satisfy_one())
#print (expr2truthtable(f1m))


# Test
# ....
#   The formula
#   f-> = ( ~a & ~b & ~c & ~d ) | ( ~a & ~b & c & ~d ) | ( a & ~b & ~c & d ) | ( ~a & b & ~c & ~d )
#   produces the page 386 pdf truth table
a, b, c, d = map(bddvar, 'abcd')
f1 = ( ~a & ~b & ~c & ~d ) | ( ~a & ~b & c & ~d ) | ( a & ~b & ~c & d ) | ( ~a & b & ~c & ~d )
print ( list(f1.satisfy_all()) )
