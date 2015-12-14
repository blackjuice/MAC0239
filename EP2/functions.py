    
# Algoritmo exists
def Exists(Bf, x):
    return (Bf.restric({x: 0}) & Bf.restrict({x: 1}))

# Algoritmo SAT
def SAT(phi, S):    
    if (phi.kind == "1"):
        return S

    if (phi.kind == "0"):
        return None

    if (phi.child[0] == None and phi.child[1] == None):
        return  phi.kind & S.restrict({phi.kind:1})
 
    if (phi.kind == "-"):
        return (phi.child[0] & S.restrict({phi.child[0]: 0}))

    if (phi.kind == "+" and phi.child[0] != None and phi.child[1] ~= None):
        return(SAT(phi.child[0], S) | (SAT(phi.child[1], S)) 

    if (phi.kind == "*" and phi.child[0] != None and phi.child[1] ~= None):
        return(SAT(phi.child[0], S) & (SAT(phi.child[1], S)) 

    if (phi.kind == "AX"):
        return(SAT(CTLfree.parse("- EX -" + str(phi.child[0])), S))

    if (phi.kind == "AU"):
        string = "+-(EU + -" + str(phi.child[0]) + ")(*(-" + str(phi.child[0]) + ")(-" + str(phi.child[1]) + "))(EG -" + str(phi.child[1]) + ")"
        return(SAT(CTLfree.parse(string), S))

    if (phi.kind == "EX"):
        return(SAT_EX(phi.child[0], S))

    if (phi.kind == "EU"):
        return(SAT_EU(phi.child[0], phi.child[1], S))

    if (phi.kind == "EF"):
        return(SAT(CTLfree.parse("EU(1)(" + str(phi.child[0]) + ")"), S))

    if (phi.kind == "EG"):
        return(SAT(CTLfree.parse("- AF -" + str(phi.child[0])), S))

    if (phi.kind == "AF"):
        return(SAT_AF(phi.child[0], S))

    if (phi.kind == "AG"):
        return(SAT(CTLfree.parse("- EF -" + str(phi.child[0])), S))


def SAT_AF(phi, S):
    X = S
    Y = SAT(phi, S)
    while (X != Y):
        X = Y
        Y = Y | Pre_forte(Y)
    return (Y)

def SAT_EU(phi, psi, S):
    W = SAT(phi, S)
    Y = SAT(psi, S)
    X = S
    while (X != Y):
        X = Y  
        Y = Y | (W & Pre_fraca(Y))
    return (Y)    

def SAT_EX(phi, S):
    X = SAT(phi, S)
    Y = Pre_fraca(X)
    return Y

    
