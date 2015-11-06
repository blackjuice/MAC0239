from pyeda.inter import *
from subprocess import call
import os


def Export2Image(b, fmt, file_name):
    # Exporta o diagrama para o Graphviz (linguagem Dot)
    with open('temp.gv', 'w') as hFile:
        hFile.write(b.to_dot())
    # Gera o PDF com o diagrama
    call(['dot', '-T' + fmt, 'temp.gv', '-o' + file_name])
    os.remove('temp.gv')

n, k = [int(j) for j in input("Enter two numbers here: ").split()]

X = exprvars("x", n, n)

print(X)

if (k == 0):
    # Row constraint
    R = And(*[OneHot(*[X[r,c] for c in range(n)]) for r in range(n)])
    
    # Column constraint
    C = And(*[OneHot(*[X[r,c] for r in range(n)]) for c in range(n)])
    
    # Diagonal constraint (Left - Rigth)
    starts = [(i, 0) for i in range(n-2, 0, -1)] + [(0, i) for i in range(n-1)]
    lrdiags = []
    for r, c in starts:
        lrdiags.append([])
        ri, ci = r, c
        while ri < n and ci < n:
            lrdiags[-1].append((ri, ci))
            ri += 1
            ci += 1

    DLR = And(*[OneHot0(*[X[r,c] for r, c in diag]) for diag in lrdiags])

    # Diagonal constraint (Rigth - Left)
    starts = [(i, n-1) for i in range(n-2, -1, -1)] + [(0, i) for i in range(n-2, 0, -1)]
    rldiags = []
    for r, c in starts:
        rldiags.append([])
        ri, ci = r, c
        while ri < n and ci >= 0:
            rldiags[-1].append((ri, ci))
            ri += 1
            ci -= 1

    DRL = And(*[OneHot0(*[X[r,c] for r, c in diag]) for diag in rldiags])

    S = R & C & DLR & DRL

if (k > 0):
    # Row constraint
    R = And(*[OneHot(*[X[r,c] for c in range(n)]) for r in range(n)])

    # Column constraint
    C = And(*[OneHot(*[X[r,c] for r in range(n)]) for c in range(n)])
    
    # Diagonal constraint (Left - Rigth)
    starts = [(i, 0) for i in range(n-2, 0, -1)] + [(0, i) for i in range(n-1)]
    lrdiags = []
    for r, c in starts:
        lrdiags.append([])
        ri, ci = r, c
        while ri < n and ci < n:
            lrdiags[-1].append((ri, ci))
            ri += 1
            ci += 1

    DLR = And(*[OneHot0(*[X[r,c] for r, c in diag]) for diag in lrdiags])

    # Diagonal constraint (Rigth - Left)
    starts = [(i, n-1) for i in range(n-2, -1, -1)] + [(0, i) for i in range(n-2, 0, -1)]
    rldiags = []
    for r, c in starts:
        rldiags.append([])
        ri, ci = r, c
        while ri < n and ci >= 0:
            rldiags[-1].append((ri, ci))
            ri += 1
            ci -= 1

    DRL = And(*[OneHot0(*[X[r,c] for r, c in diag]) for diag in rldiags])

    for i in range(0, k):
        x, y = [int(j) for j in input("Enter two numbers here: ").split()]
        R.restrict({X[x][y]: 1})
        C.restrict({X[x][y]: 1})
        DLR.restrict({X[x][y]: 1})
        DRL.restrict({X[x][y]: 1}) 

    S = R & C & DLR & DRL

S = S.to_cnf()
bdd = expr2bdd(S)
Export2Image(bdd, 'pdf', 'bdd1.pdf')
#print(S.is_cnf())
#print(S.is_zero())

print(len(S.xs))
print (S)
