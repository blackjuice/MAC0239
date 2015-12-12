# MAC0239 - Introdução à Lógica e Verificação de Programas

* Get recommended [Python](https://www.python.org/) version, or `sudo apt-get install python3-dev`;
* [Installing PyEDA](http://pyeda.readthedocs.org/en/latest/bdd.html);
* [Getting Graphviz - Graph Visualization Software](http://www.graphviz.org/pub/graphviz/stable/SOURCES/graphviz-2.38.0.tar.gz);
* **NOTE:** to use python 3rd version, execute python with `python3`.
* **NOTE:** to get pip: ``sudo apt-get install python3-pip``. To install PyEDA with pip3: instead of``pip3 install pyeda``, go with ``pip-3.2 install pyeda``

## Reference:

* [Solve a N-Queens Problem Using a SAT Solver](https://sites.google.com/site/haioushen/search-algorithm/solvean-queensproblemusingsatsolver);
* [Python script to solve N-Queen problem using minisat](http://forrestbao.blogspot.com.br/2007/11/python-script-to-solve-n-queen-problem.html);
* Might be worth our time: [.pdf](http://www.gcn.us.es/7BWMC/volume/21_queens.pdf)

To play on 8x8: [click me!](http://www.brainmetrix.com/8-queens/)

Not sure if this helps...

```python
    def queensproblem(rows, columns):
        solutions = [[]]
        for row in range(rows):
            solutions = add_one_queen(row, columns, solutions)
        return solutions

    def add_one_queen(new_row, columns, prev_solutions):
        return [solution + [new_column]
                for solution in prev_solutions
                for new_column in range(columns)
                if no_conflict(new_row, new_column, solution)]

    def no_conflict(new_row, new_column, solution):
        return all(solution[row]       != new_column           and
                   solution[row] + row != new_column + new_row and
                   solution[row] - row != new_column - new_row
                   for row in range(new_row))

    for solution in queensproblem(8, 8):
        print(solution)
```

