# CNYT-2020-2
# Classic To Quantum

This is a repository that has some different functions to perform some operations for diferent systems.

The operations this library does are:

- Calculate positions in deterministic systems.
- Calculate probabilities in probabilistic systems.
- Calculate probabilities in Quantum systems.
- Plot probabilites of Quantum systems status vectors.


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

- Also you have to install Numpy, Scipy and Matplotlib

This is a video where you can leran how to install them [Installing libraries](https://www.youtube.com/watch?v=oE4KeuVNqcQ)

If you are using Pycharm it will install them for you in your program.

## Running the tests
For running the predetermined test you have to open the file **testsClassicToQuantum.py** in your prefered IDE and then just run it, then it will show you the results from the tests.

- For deterministic systems:

If you want to use a function by your own, you just have to open the file **classToQuan.py** and run it using this sintax:
```python
m = [[c, d], [e, f]]			 # Boolean matrix
v = [[a], [b]]                           # Real vector
t = s					 # Integer
function_name(m, v, t)
```

- For probabilistic systems:

If you want to use a function by your own, you just have to open the file **classToQuan.py** and run it using this sintax:
```python
m = [[i, j], [k, l]]	 	         # Real matrix
v = [[a], [b]]                           # Real vector
t = s					 # Integer
function_name(m, v, t)
```

- For quantum systems:

If you want to use a function by your own, you just have to open the file **classToQuan.py** and run it using this sintax:
```python
m2 = [[[i, j], [k, l]], [[m, n], [o, p]]] # Complex matrix
v1 = [[a, b], [c, d]]                     # Complex vector
t = s			        	  # Integer
function_name(m, v, t)
```

- For plots:

If you want to use a function by your own, you just have to open the file **classToQuan.py** and run it using this sintax:
```python
v = [a, b, c, d]                 # Real vector
function_name(v)
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
