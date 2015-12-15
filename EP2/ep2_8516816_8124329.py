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


# construindo agora o Bx', que devolve
# uma lista de todos os estados envolvidos
def write_array_B_prime (ddt, modeloPhi):
    array_b_prime = [0] * len(ddt)

    if (modeloPhi == "0" or modeloPhi == "1"):
        return modeloPhi

    j = 0; b_prime = ""; guarda_operador = ""; guarda_proposicao = False;
    for c in modeloPhi:
        if (c == "+" or c == "*"):
            guarda_operador = c

    modeloPhi_array = array_muda_sinal ( array_all_int (modeloPhi) , modeloPhi)

    # percorre dicionario e procura todas as proposicoes
    # envolvidas no modelo
    for i in range(numeroEstados):
        array_tmp = array_muda_sinal ( (array_all_int (ddt[i])) , ddt[i])

        if guarda_operador != "":
            if (guarda_operador == "*"):
                for s in range( len(modeloPhi_array) ):
                    hold = False
                    if modeloPhi_array[s] in array_tmp:
                        hold = True
                    else: break;
            if (guarda_operador == "+"):
                for s in range( len(modeloPhi_array) ):
                    hold = False
                    if modeloPhi_array[s] in array_tmp:
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


# Calcula S - X (recebe X como parametro)
def calcula_S_minus_X (ddt, modeloPhi):
    s_minus_x_OLD = [0] * (2 * len(ddt)); s = 0;
    array_b_prime = write_array_B_prime (ddt, modeloPhi)

    for i in range( len(ddt) ):
        for j in range( len(array_b_prime) ):
            if convert_X_to_Xprime (ddt[i]) != array_b_prime[j]:
                hold = True
            else:
                hold = False; break;

        if hold == True:
            s_minus_x_OLD[s] = convert_X_to_Xprime (ddt[i])
            s = s + 1

    s_minus_x = [0] * s
    for i in range(s):
        s_minus_x[i] = s_minus_x_OLD[i]

    return (s_minus_x)

# Calculo da pre imagem fraca
def Pre_fraca (kripke, ddt, array_b_prime):
    kripke = ( separaParenteses_em_grupos (kripke) )
    len_kripke = len(kripke)
    lst1 = [0] * len_kripke
    lst2 = [0] * len_kripke
    b_arrow = ""
    #array_b_prime = write_array_B_prime (ddt, modeloPhi)

    for i in range( len_kripke ):
        # lista temporaria contem os pares kripkes
        lst_tmp = array_all_int (kripke[i])
        # Do par(f,g), fazemos str_tmp = X[i] & X'[j]
        lst1[i] = ddt[ lst_tmp[0] ]
        lst2[i] = convert_X_to_Xprime ( ddt[ lst_tmp[1] ] )

    # fazendo a conta
    for i in range( len_kripke ):
        lado1 = expr2bdd( expr(lst2[i]) )

        for j in range( len(array_b_prime) ):
            lado2 = expr2bdd( expr(array_b_prime[j]) )
            str_tmp = ""

            f = (lado1) & (lado2)
            if (f.is_zero() != True):
                str_tmp = lst1[i]
                b_arrow = b_arrow + " | " + str_tmp
                #print (str_tmp)

    b_arrow = b_arrow[3:] # apagando 3 primeiros char
    return (b_arrow)

def Pre_forte (b_s, kripke, ddt, modeloPhi):
    array_b_prime = calcula_S_minus_X (ddt, modeloPhi)
    b_result = b_s + " | ~(" + Pre_fraca (kripke, ddt, array_b_prime) + ")"
    return (b_result)



#-----------ALGORITMOS SAT----------------------------------------------

def SAT(phi, S):    
    if (phi.kind == "1"):
        return S

    if (phi.kind == "0"):
        return None

    if (phi.child[0] == None and phi.child[1] == None):
        return  phi.kind & S.restrict({phi.kind:1})
 
    if (phi.kind == "-"):
        SAT(phi.child[0], S)

    if (phi.kind == "+" and phi.child[0] != None and phi.child[1] != None):
        return(SAT(phi.child[0], S) | (SAT(phi.child[1], S)) 

    if (phi.kind == "*" and phi.child[0] != None and phi.child[1] != None):
        return(SAT(phi.child[0], S) & (SAT(phi.child[1], S)) 

    if (phi.kind == "AX"):
        return(SAT(CTLfree.parse("- EX -" + str(phi.child[0])), S))

    if (phi.kind == "AU"):
        string = "+-(EU + -" + str(phi.child[0]) + ")(*(-" + str(phi.child[0]) + ")(-" + str(phi.child[1]) + "))(EG -" + str(phi.child[1]) + ")"
        SAT(CTLfree.parse(string), S)

    if (phi.kind == "EX"):
        SAT_EX(phi, S)

    if (phi.kind == "EU"):
        SAT_EU(phi.child[0], phi.child[1], S)

    if (phi.kind == "EF"):
        SAT(CTLfree.parse("EU(1)(" + str(phi.child[0]) + ")"), S)

    if (phi.kind == "EG"):
        SAT(CTLfree.parse("- AF -" + str(phi.child[0])), S)

    if (phi.kind == "AF"):
        SAT_AF(phi.child[0], S)

    if (phi.kind == "AG"):
        SAT(CTLfree.parse("- EF -" + str(phi.child[0])), S)


def SAT_AF(phi, S):
    X = S
    Y = SAT(phi, S)
    while (X ~= Y):
        X = Y
        Y = Y | Pre_forte(Y)
    return (Y)

def SAT_EU(phi, psi, S):
    W = SAT(phi, S)
    Y = SAT(psi, S)
    X = S
    while (X ~= Y):
        X = Y  
        Y = Y | (W & Pre_fraca(Y))
    return (Y)    
    
def SAT_EX(phi, S):
    X = SAT(phi, S)
    Y = Pre_fraca(X)
    return Y

    


#------------main------------------------------------------------------------
numeroEstados = int(input())
kripke = input()
rotulos = input()
formulaCTL = CTLtree( input() )
interest = input()

# criando dicionario
ddt = default_ddt_value (rotulos, numeroEstados)

# atualizamos dicionario
ddt = update_ddt_value (rotulos, numeroEstados, ddt)

# construimos Bs
b_s = write_B_s (ddt)
S = expr2bdd( expr(b_s) ) # conversao para BDD

# Aplicacao do algoritmo SAT
if SAT(formulaCTL, S).satisfy_one() == None:
    print ("UNSAT")
else:
    print ("SAT")
    print ("lista de todos os estados que SAT:")
    print (list( SAT(phi, S).satisfy_all() ))

'''
array_b_prime = write_array_B_prime (ddt, modeloPhi)
Pre_fraca (kripke, ddt, array_b_prime)
print (Pre_fraca (kripke, ddt, array_b_prime))
Pre_forte (b_s, kripke, ddt, modeloPhi)
'''
