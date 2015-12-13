'''
  integrantes:
    Leonardo Daneu Lopes (8516816)
    Lucas Sung Jun Hong  (8124329)

'''
from parser import CTLtree
#from subprocess import call
from pyeda.inter import *
import os
import re
#------------main--------------
'''
'''
numeroEstados = input()
kripke = input()
rotulos = input()
formulaCTL = str( CTLtree( input() ) ) #formulaCTL = input(); formulaCTL = str( CTLtree(formulaCTL) )
interest = input()

'''
Tipo 1: Sem regex (problema quando i > 9)
-----------------------------------------
    real    0m0.892s
    user    0m0.560s
    sys     0m0.056s
print (rotulos)
'''
#rotulos = "[(“x1”,”x2”),(“x2”,“x3”),(“x100”)]"
m1 = " ".join(rotulos)
#m1 = m1 * 1000
a = [int(s) for s in m1.split() if s.isdigit()]
print (a)
print(max(a))

'''
Tipo 2: Com regex
-----------------------------------------
    real    0m0.413s
    user    0m0.384s
    sys     0m0.028s

'''
#rotulos = "[(“x1”,”x2”),(“x2”,“x3”),(“x100”)]"
m2 = re.sub(r'\D', " ", rotulos)
m2 = m2 * 10000
a = [int(s) for s in m2.split() if s.isdigit()]
print (a)
print(max(a))
