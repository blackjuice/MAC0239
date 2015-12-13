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

#------------functions--------------

# devolve uma lista com todos os inteiros envolvidos em um string
# uso highProposicao (rotulos)
def highProposicao (str):
    str_tmp = re.sub(r'\D', " ", str)
    high_Xi = [int(s) for s in str_tmp.split() if s.isdigit()]
    #print(max(high_Xi)); return int( max(high_Xi) )
    return (high_Xi)

# Standard valor no dicionario
def default_ddt_value (rotulos, numeroEstados):
    # criando uma conjuncao com todas as proposicoes envolvidas
    high_Xi = int ( max(highProposicao (rotulos)) ) # maior proposicao
    str_all_value = "~X[0]"
    for i in range( 1, high_Xi ):
        str_all_value = str_all_value + " & " + "~" + "X[" + str(i) + "]"

    # Todos os valores do dicionario contem conjuncao do tipo Phi( ~x_i )
    # com i = 0..N-1
    str_tmp = "" # limpando str_tmp
    str_tmp = [i for i in range( numeroEstados) ]
    ddt = {el:str_all_value for el in str_tmp}
    return (ddt)

# Atualizacao do dicionario
def update_ddt_value (arrayStr_listaEstados, numeroEstados, ddt):
    for i in range( numeroEstados ):
        array_tmp = ""
        # Lemos um rotulo por vez
        array_tmp = highProposicao ( arrayStr_listaEstados[i] )

        # Se estado/rotulo nao for vazio, continue:
        if len(array_tmp) != 0:
            # verificamos cada proposicao
            for j in range( len(array_tmp) ):
                str_tmp = "" # limpamos str_tmp
                str_tmp_new = "X[" + str( array_tmp[j] - 1 ) + "]"
                str_tmp = "~" + str_tmp_new

                # atualizamos o value do key[i]
                resposta = ddt[i].replace(str_tmp, str_tmp_new)
                ddt[i] = resposta
        else:
            print ("empty")

    print (ddt)
    return (ddt)

#------------main--------------
numeroEstados = int(input())
kripke = input()
rotulos = input()
formulaCTL = str( CTLtree( input() ) )
interest = input()

X = bddvars("x", 3)

# criando dicionario
ddt = default_ddt_value (rotulos, numeroEstados)

# guarda todos os estados em uma lista
arrayStr_listaEstados = re.findall("\((.*?)\)", rotulos)

# atualizamos dicionario
ddt = update_ddt_value (arrayStr_listaEstados, numeroEstados, ddt)
'''

'''
