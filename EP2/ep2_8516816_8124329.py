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
import string
#------------main--------------
'''
'''
numeroEstados = int(input())
kripke = input()
rotulos = input()
formulaCTL = str( CTLtree( input() ) ) #formulaCTL = input(); formulaCTL = str( CTLtree(formulaCTL) )
interest = input()

# devolve uma lista com todos os inteiros envolvidos em um string
# uso highProposicao (rotulos)
def highProposicao (str):
    str_tmp = re.sub(r'\D', " ", str)
    high_Xi = [int(s) for s in str_tmp.split() if s.isdigit()]
    #print(max(high_Xi)); return int( max(high_Xi) )
    return (high_Xi)


# criando uma conjuncao com todas as proposicoes envolvidas
high_Xi = int ( max(highProposicao (rotulos)) )
print (high_Xi)
X = bddvars("x", 3)
str_all_value = "~X[0]"
for i in range( 1, high_Xi ):
    str_all_value = str_all_value + " & " + "~" + "X[" + str(i) + "]"
print (str_all_value)

'''
cada um tem o negocio certo
agora preciso ler da lista de rotulos e separar cada () como um grupo
'''
#numeroEstados = 2

# colocando str_all_value como valores no dicionario,
# com cada key como um i, tal que i = 0..N-1
str_tmp = "" # limpando str_tmp
str_tmp = [i for i in range( numeroEstados) ]
ddt = {el:str_all_value for el in str_tmp}
print (ddt)

# guarda todos os estados em uma lista
print (rotulos)
arrayStr_listaEstados = re.findall("\((.*?)\)", rotulos)
print ( arrayStr_listaEstados, len(arrayStr_listaEstados) )

here = "NEW"
#resposta = re.sub( r"\((.*?)\)", "[(“x1”,”x2”),(“x2”,“x3”),(“x3”)]", here )
resposta = re.sub( r"\((.*?)\)", here, "[(“x1”,”x2”),(“x2”,“x3”),(“x3”)]" )
print ( resposta )
'''
if (len(arrayStr_listaEstados) == numeroEstados):
    print ("numero de rotulos == numero de estados!!!")
else:
    print ("numero de rotulos != numero de estados!!!")
'''
'''


str_tmp_new = "X[" + str( i ) + "]"
str_tmp = "~" + str_tmp_new
print ( str_tmp_new )
print ( str_tmp )
'''
# percorro cada rotulo
for i in range( numeroEstados ): #for i in range( len(arrayStr_listaEstados) ):
    # Lemos um rotulo por vez
    array_tmp = highProposicao ( arrayStr_listaEstados[i] )

    # Se estado/rotulo nao for vazio, continue:
    if len(array_tmp) != 0:
        # verificamos cada proposicao
        for j in range( len(array_tmp) ):
            str_tmp = "" # limpamos str_tmp
            
            str_tmp_new = "X[" + str( array_tmp[j] - 1 ) + "]"
            str_tmp = "~" + str_tmp_new
            #print ( str_tmp_new ); print ( str_tmp )

            # atualizamos o value do key[i]
            resposta = ddt[i].replace(str_tmp, str_tmp_new)
            #print ("dicionario = " + ddt[0] + str(i))
            # substituimos ~X[j] por X[j] se conter no estado            
            #resposta = re.sub( r"\((.*?)\)", here, "[(“x1”,”x2”),(“x2”,“x3”),(“x3”)]" )
            #print (resposta)

            ddt[i] = resposta


    else:
        print ("empty")

print (ddt)
