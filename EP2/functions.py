# Algoritmo apply
    # Bf = Bx', Bg = B->
    def Apply(op, Bf, Bg):
        str = Bf + str(op) + Bg
        if (Bf.lo ~= None and Bf.hi ~= None) and (Bg.lo ~= None and Bg.hi ~= None):
            Apply(op, Bf.hi, Bg.hi)
            Apply(op, Bf.lo, Bg.lo)
        if (Bf.lo ~= None and Bf.hi ~= None) and (Bg.lo == None and Bg.hi == None):
            Apply(op, Bf.hi, Bg)
            Apply(op, Bf.lo, Bg)
        if (Bf.lo == None and Bf.hi == None) and (Bg.lo ~= None and Bg.hi ~= None):
            Apply(op, Bf, Bg.hi)
            Apply(op, Bf, Bg.lo)
        if (Bf.lo == None and Bf.hi == None) and (Bg.lo == None and Bg.hi == None):  
            str = Bf + str(op) + Bg
        return (str)
    # Algoritmo exisits
    def Exists(op, Bf, x):
        return Apply(op, Bf.restric(x, 0), Bf.restrict(x, 1))
    
