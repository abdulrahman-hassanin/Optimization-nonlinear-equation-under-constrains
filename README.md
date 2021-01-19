# Cost Function Optimization

## Introduction

A python program aims to minimize a nonlinear cost function f(x,y) given two nonlinear constrains g1(x,y) and g2(x,y), where g1,2(x,y)<0.

[Sequential Least SQuares Programming (SLSQP)](https://docs.scipy.org/doc/scipy/reference/tutorial/optimize.html#sequential-least-squares-programming-slsqp-algorithm-method-slsqp) Algorithm used for optimization.

## Requirments

```python
pip install numpy
pip install scipy
pip install matplotlib
```

## Usage

* Run optimize.py file

```python
python optimize.py
```

* Enter the cost function equation.
* Enter the two constrains g1(x,y) and g2(x,y) equations.
* Enter the initial point value of (x,y).

* Returns
    * A plot window appears of f(x,y), g1(x,y), and g2(x,y) vs iteration index.
    * The final minimized value of the cost function and the final point (x,y) will be printed.

## Important Dependencies

* Equations must be written within x and y variables.
* supported operations as following:
    * add '+'
    * sub '-'
    * mul '*'
    * divide '/'
    * power '^'
    * Example: 2 * x**2 + 3 * y - 10