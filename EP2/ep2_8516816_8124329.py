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
    return (high_Xi)

# recebe um array de inteiro
# e devolve o array com sinais
def array_muda_sinal (array_tmp, str):
    i = 0; guarda_sinal = False
    for c in str:
        if (c == "-" or c == "~"):
            guarda_sinal = True

        if c.isdigit():
            if guarda_sinal == True:
                array_tmp[i] = -array_tmp[i]
            i = i + 1
            guarda_sinal = False
    return array_tmp

# Standard valor no dicionario
def default_ddt_value (rotulos, numeroEstados):
    # criando uma conjuncao com todas as proposicoes envolvidas
    high_Xi = int ( max(array_all_int (rotulos)) ) + 1 # maior proposicao
    str_all_value = "~X[1]"
    for i in range( 2, high_Xi ):
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
    for i in range(numeroEstados):
        array_tmp = ""
        # Lemos um rotulo por vez
        array_tmp = array_all_int ( arrayStr_listaEstados[i] )

        # Se estado/rotulo nao for vazio, continue:
        if len(array_tmp) != 0:
            # verificamos cada proposicao
            for j in range( len(array_tmp) ):
                str_tmp = "" # limpamos str_tmp
                str_tmp_new = "X[" + str( array_tmp[j] ) + "]"
                str_tmp = "~" + str_tmp_new

                # atualizamos o value do key[i]
                str_tmp = ddt[i].replace(str_tmp, str_tmp_new)
                ddt[i] = str_tmp

    return (ddt)

# Converte X para Y (ou X')
def convert_X_to_Xprime (str_tmp):
    str_tmp = str_tmp.replace("X", "Y")
    return str_tmp

# write Bs
def write_B_s (ddt):
    b_s = ""
    for i in range(len(ddt)):
        # atualiza b_s
        b_s = b_s + " | " + ddt[i]
    b_s = b_s[3:] # apagando 3 primeiros char
    return (b_s)

# Calculo da pre imagem fraca
def Pre_fraca (kripke, ddt, modeloPhi):
    kripke = ( separaParenteses_em_grupos (kripke) )
    len_kripke = len(kripke)
    lst1 = [0] * len_kripke
    lst2 = [0] * len_kripke
    b_arrow = ""

    for i in range( len_kripke ):
        # lista temporaria contem os pares kripkes
        lst_tmp = array_all_int (kripke[i])
        # Do par(f,g), fazemos str_tmp = X[i] & X'[j]
        lst1[i] = ddt[ lst_tmp[0] ]
        lst2[i] = convert_X_to_Xprime ( ddt[ lst_tmp[1] ] )

    array_b_prime = write_array_B_prime (ddt, modeloPhi)
    print ( array_b_prime)

    for i in range( len_kripke ):
        lado1 = expr2bdd( expr(lst2[i]) )

        for j in range( len(array_b_prime) ):
            lado2 = expr2bdd( expr(array_b_prime[j]) )
            str_tmp = ""
            print (lst1[i], "= * =", lst2[i], "= * =", array_b_prime[j])

            f = (lado1) & (lado2)
            if (f.is_zero() != True):
                str_tmp = lst1[i]
                b_arrow = b_arrow + " | " + str_tmp

    b_arrow = b_arrow[3:] # apagando 3 primeiros char
    b_arrow_BDD = expr2bdd( expr(b_arrow) )
    return (b_arrow_BDD)

# construindo agora o Bx'
def write_array_B_prime (ddt, modeloPhi):
    array_b_prime = [0] * len(ddt)

    if (modeloPhi == "0" or modeloPhi == "1"):
        return modeloPhi

    j = 0; b_prime = ""; guarda_operador = ""; guarda_proposicao = False;
    for c in modeloPhi:
        if (c == "+" or c == "*"):
            guarda_operador = c

    array_tmp = array_all_int (modeloPhi)
    modeloPhi_array = array_muda_sinal (array_tmp, modeloPhi)

    # percorre dicionario e procura todas as proposicoes
    # envolvidas no modelo
    for i in range(numeroEstados):
        array_tmp = array_muda_sinal ( (array_all_int (ddt[i])) , ddt[i])

        if guarda_operador != "":
            if (guarda_operador == "*"):
                for j in range( len(modeloPhi_array) ):
                    hold = False
                    if modeloPhi_array[j] in array_tmp:
                        hold = True
                    else: break;
            if (guarda_operador == "+"):
                for j in range( len(modeloPhi_array) ):
                    hold = False
                    if modeloPhi_array[j] in array_tmp:
                        hold = True; break;

        else:
            hold = False
            if modeloPhi_array[0] in array_tmp:
                hold = True

        if hold == True:
            array_b_prime[j] = convert_X_to_Xprime (ddt[i])
            j = j + 1

    new_array_b_prime = [0] * j
    for i in range(j):
        new_array_b_prime[i] = array_b_prime[i]

    return new_array_b_prime





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

        #guarda_conjunto_b_arrow

        # atualiza b_arrow
        b_arrow = b_arrow + " | " + str_tmp

    b_arrow = b_arrow[3:] # apagando 3 primeiros char
    return (b_arrow)

# construindo agora o Bx'
def write_B_xPrime (ddt, modeloPhi):

    if (modeloPhi == "0" or modeloPhi == "1"):
        return modeloPhi

    i = 0; b_prime = ""; guarda_operador = ""; guarda_proposicao = False;
    for c in modeloPhi:
        if (c == "+" or c == "*"):
            guarda_operador = c

    array_tmp = array_all_int (modeloPhi)
    modeloPhi_array = array_muda_sinal (array_tmp, modeloPhi)

    # percorre dicionario e procura todas as proposicoes
    # envolvidas no modelo
    for i in range(numeroEstados):
        array_tmp = array_muda_sinal ( (array_all_int (ddt[i])) , ddt[i])

        if guarda_operador != "":
            if (guarda_operador == "*"):
                for j in range( len(modeloPhi_array) ):
                    hold = False
                    if modeloPhi_array[j] in array_tmp:
                        hold = True
                    else: break;
            if (guarda_operador == "+"):
                for j in range( len(modeloPhi_array) ):
                    hold = False
                    if modeloPhi_array[j] in array_tmp:
                        hold = True; break;

        else:
            hold = False
            if modeloPhi_array[0] in array_tmp:
                hold = True

        if hold == True:
            b_prime = b_prime + " | " + ddt[i]

    b_prime = b_prime[3:] # apagando 3 primeiros char
    b_prime = convert_X_to_Xprime (b_prime)
    return b_prime



#------------main--------------
numeroEstados = int(input())
kripke = input()
rotulos = input()
#formulaCTL = str( CTLtree( input() ) )
formulaCTL = CTLtree( input() )
interest = input()

#X = bddvars("x", numeroEstados + 1)
#Y = bddvars("y", numeroEstados + 1)
#print (X)

# criando dicionario
ddt = default_ddt_value (rotulos, numeroEstados)
#print (ddt); print ()

# atualizamos dicionario
ddt = update_ddt_value (rotulos, numeroEstados, ddt)
#print (ddt)

# construimos Bs
b_s = write_B_s (ddt)
#print (b_s)

# construimos B->
b_arrow = write_B_arrow (kripke, ddt)




# construimos Bx
#   exemplos para testar modelos
modeloPhi = "+(x1)(x2)"; print (modeloPhi)
#modeloPhi = "x2"; print (modeloPhi)
#    modeloPhi = "1"; print (modeloPhi)
b_prime =  write_B_xPrime (ddt, modeloPhi)
#print (b_prime)

print (Pre_fraca (kripke, ddt, modeloPhi))



#def Pre_forte(modeloPhi):
