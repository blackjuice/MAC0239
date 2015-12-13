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
'''
numeroEstados = input()
kripke = input()
rotulos = input()
formulaCTL = str( CTLtree( input() ) ) #formulaCTL = input(); formulaCTL = str( CTLtree(formulaCTL) )
interest = input()

numeroEstados = 10
# Tipo 1
dt = {0: ()} # inicializando dicionario temporario
for i in range( int(numeroEstados) ):
    dictionary = {i: ''}
    print (i, dictionary)
    dt.update( dictionary )
    dictionary.update( dt )
print (dictionary)

# Tipo 2
lst = [i for i in range( int(numeroEstados) )] * 1
print (lst)
ddt = {el:0 for el in lst}
print (ddt)

# Tipo 3
lst3 = [i for i in range( int(numeroEstados) )] * 1
ddt.fromkeys(lst3)
print (ddt)

# Tipo 4
lst4 = [0 for i in range( int(numeroEstados) )]
ddt.fromkeys(lst3)
print (ddt)
