# prime-tables
Appplication that takes numeric input (N) from a user and outputs a multiplication table of (N) prime numbers

## How to run

The application requires Python 3 and can be run directly from the console.

```
 python3 main.py
```

To run tests, nose (Python 3) is required. Optionally, a coverage plugin for nose can also be installed:
```
⇒  nosetests3 --with-coverage
...............      
Name              Stmts   Miss  Cover   Missing
-----------------------------------------------
eratosthenes.py      14      0   100%
grid.py              29      0   100%
main.py              15      4    73%   13, 15-16, 19
-----------------------------------------------
TOTAL                58      4    93%
----------------------------------------------------------------------
Ran 15 tests in 2.838s

OK

```

## Features

* code is simple, built only with the standard library
* code uses intuitive names for classes, functions and variables
* code uses an algorithm that has been extensively studied

## Optimizations

* optimize how 2d arrays are built/initialized, perhaps using a library such as numpy
* optimize the sieve (for example, implementing the segmented version instead)
* create html output on top of current console one, perhaps using a library such as yattag
