Exemplo:

    N                                       // número de estados
    [(n1,n2),(n3,n4), ...]                  // lista de pares, arestas do modelo de Kripke
    [(“x1”,”x2”, …),(“x2”, ... “x4”),...]   // lista com os rótulos dos N estados
    AF EU(+(EG x1)(x2))(AF x1)              // fórmula CTL a ser testada
    k                                       // estado k de interesse

## Testes de entrada

Modelo A:

    4
    [(0,1),(0,2),(1,1),(1,2),(2,0),(2,1),(2,2),(3,0),(3,1),(3,3)]
    [(“x1”,”x2”),(“x1”),(),(“x2”)]
    AG +(x1)(­x2)
    (“x1”)

Modelo B:

    3
    [(0,2),(1,0),(1,1),(2,0),(2,1)]
    [(“x1”),(“x2”),()]
    EU(x2)(x1)
    (“x2”)
