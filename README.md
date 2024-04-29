# sat-solving-2024s
Solutions to the programming exercises in the subject "SAT Solving and Extensions" at TU Vienna in the summer semester of 2024.

## Exercise 1: N-Queens DIMACS Generator
The task is to implement a generator for the N-Queens problem in DIMACS format. The generator should take an integer n as input and output a DIMACS file that represents the N-Queens problem for a chessboard of size n x n.
In order to generate the DIMACS file the following command needs to be executed:
```
python3 n_queens_generator.py n
```
where n is the size of the chessboard. The output file will be named `queens_{n}.cnf`.

The result was manually verified for instances n in [3,10] with the SAT solver [CaDiCaL](https://github.com/arminbiere/cadical).
