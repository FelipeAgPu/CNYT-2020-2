# CNYT-2020-2
# Complex Calculator

This is a repository that has some different functions to perform some operations between complex numbers.

The operations this library does are:

## For complex numbers:
- Addition
- Substraction
- Multiplication
- Division
- Module
- Conjugated
- Convert from Cartesian coordinates to Polar coordinates and vice versa.
- Phase

## For complex vectors:
- Addition
- Substraction
- Additive Inverse
- Multiplication by a scalar
- Dot product
- Norm
- Distance between two vectors

## For complex matrices:
- Addition
- Additive Inverse
- Multiplication by a scalar
- Multiplication by a matrix
- Action of a matrix
- Verify that the matrix is unitary
- Verify that the matrix is hermitian

## For complex vectors and matrices:
- Transpose
- Conjugated
- Adjoint
- Tensor product

## Getting Started

- You have to clone this library for using it in your PC.
- Then you have to move it to the folder you want.



- Cloning the library

You have to write this in your Git cmd(If you do not have Git on your computer you can install it [Here](https://git-scm.com/))
```git bash
$ git clone https://github.com/FelipeAgPu/CNYT-2020-2.git
```

In this moment you will have the repository in your PC
### Prerequisites

- You will need to have instaled Python 3.8 in your computer

Here is a link where you can download and install it:

[Python Official Page](https://python.org/)

- Be sure you have the library is in the same folder of the project you want to implement it.

## Running the tests
For running the predetermined test you have to open the file **test.py** or **test2.py** in your prefered IDE and then just run it, then it will show you the results from the tests.

- For complex numbers:

If you want to use a function by your own, you just have to open the file **complex.py** and run it using this sintax:
```python
a = [3, 1]
b = [4, -1]
function_name(a, b)
# a and b must be arrays
```

- For complex vectors:

If you want to use a function by your own, you just have to open the file **vectors_matrices.py** and run it using this sintax:
```python
v1 = [[[a, b], [c, d]]] # Complex vector
v2 = [[[e, f], [g, h]]] # Complex vector
c1 = [i, j]             # Complex Number
function_name(v1)       # For operations with one complex vector
function_name(v1, v2)   # For operations between complex vectors
function_name(c1, v2)   # For operations with a scalar
```

- For complex matrices:

If you want to use a function by your own, you just have to open the file **vectors_matrices.py** and run it using this sintax:
```python
m1 = [[[a, b], [c, d]], [[e, f], [g, h]]] # Complex matrix
m2 = [[[i, j], [k, l]], [[m, n], [o, p]]] # Complex matrix
v1 = [[a1, b1], [c1, d1]]                 # Complex vector
c1 = [i1, j1]
function_name(m1)       # For operations with one complex matrix
function_name(m1, m2)   # For operations between complex matrices
function_name(m1, v1)   # For operations between a matrix and a vector
function_name(c1, m1)   # For operations with a scalar
```
### Break down into end to end tests

This tests are going to prove if the functions work well, for each function there will be three different tests and they should show OK in each one.
The tests should show something like this:
```python

Ran 9 tests in 0.005s

OK
```
The time can change in each run.

## Built with

These libraries were built with [Python 3.8](https://python.org/) using as IDE Pycharm.

## Authors

- Juan Felipe Aguas Pulido - Engineering Student - Bogotá, Colombia.

2020

## License
This proyect has a free use license.
