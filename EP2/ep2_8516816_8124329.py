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

# Pega uma string '[ai, .. ,aj], [bx, .. ,by], ...'
# devolve uma lista de strings: lista[0] = [ai, .. ,aj]
def separaParenteses_em_grupos (str_tmp):
    return ( re.findall("\((.*?)\)", str_tmp) )

# devolve uma lista com todos os inteiros envolvidos em um string
def array_all_int (str):
    str_tmp = re.sub(r'\D', " ", str)
    high_Xi = [int(s) for s in str_tmp.split() if s.isdigit()]
    #print(max(high_Xi)); return int( max(high_Xi) )
    return (high_Xi)

# Standard valor no dicionario
def default_ddt_value (rotulos, numeroEstados):
    # criando uma conjuncao com todas as proposicoes envolvidas
    high_Xi = int ( max(array_all_int (rotulos)) ) # maior proposicao
    str_all_value = "~X[0]"
    for i in range( 1, high_Xi ):
        str_all_value = str_all_value + " & " + "~" + "X[" + str(i) + "]"

    # Todos os valores do dicionario contem conjuncao do tipo PI( ~x_i )
    # com i = 0..N-1
    str_tmp = "" # limpando str_tmp
    str_tmp = [i for i in range( numeroEstados) ]
    ddt = {el:str_all_value for el in str_tmp}
    return (ddt)

# Atualizacao do dicionario
def update_ddt_value (rotulos, numeroEstados, ddt):
    # guarda todos os estados em uma lista
    arrayStr_listaEstados = separaParenteses_em_grupos (rotulos)

    for i in range( numeroEstados ):
        array_tmp = ""
        # Lemos um rotulo por vez
        array_tmp = array_all_int ( arrayStr_listaEstados[i] )

        # Se estado/rotulo nao for vazio, continue:
        if len(array_tmp) != 0:
            # verificamos cada proposicao
            for j in range( len(array_tmp) ):
                str_tmp = "" # limpamos str_tmp
                str_tmp_new = "X[" + str( array_tmp[j] - 1 ) + "]"
                str_tmp = "~" + str_tmp_new

                # atualizamos o value do key[i]
                str_tmp = ddt[i].replace(str_tmp, str_tmp_new)
                ddt[i] = str_tmp
    return (ddt)

# Converte X para Y (ou X')
def convert_X_to_Xprime (str_tmp):
    str_tmp = str_tmp.replace("X", "Y")
    return str_tmp

# Criamos BDD do B->
def write_B_arrow (kripke, ddt):

    kripke = ( separaParenteses_em_grupos (kripke) )
    b_arrow = ""

    for i in range( len(kripke) ):
        # lista temporaria contem os pares kripkes
        lst_tmp = array_all_int (kripke[i])
        # Do par(f,g), fazemos str_tmp = X[i] & X'[j]
        str_tmp = ( ddt[ lst_tmp[0] ] + 
                    " & " +
                    convert_X_to_Xprime ( ddt[ lst_tmp[1] ] ) )
        # atualiza b_arrow
        b_arrow = b_arrow + " | " + str_tmp

    b_arrow = b_arrow[3:] # apagando 3 primeiros char
    return (b_arrow)

#------------main--------------
numeroEstados = int(input())
kripke = input()
rotulos = input()
#formulaCTL = str( CTLtree( input() ) )
formulaCTL = CTLtree( input() )
interest = input()
X = bddvars("x", numeroEstados)
Y = bddvars("y", numeroEstados)

# criando dicionario
ddt = default_ddt_value (rotulos, numeroEstados)

# atualizamos dicionario
ddt = update_ddt_value (rotulos, numeroEstados, ddt)
#print (ddt)

# construimos B->
b_arrow = write_B_arrow (kripke, ddt)

# construindo agora o Bx', que eh mais complicado.
def write_B_xPrime (modeloPhi):


    return 0

'''
print (b_arrow)

#b_arrow = expr(b_arrow)
#b_arrow = expr2bdd(b_arrow)
#print ( b_arrow.satisfy_one() )
#print ( list( b_arrow.satisfy_all() ) )


testing
#CTLtree.parse(str)
str_tmp = "AU(AU(EX 1)(x1))(EU(x2)(0))"
print (CTLtree(str_tmp))
print (str(CTLtree.parse(str_tmp)) )
'''