# Cost Function Optimization

## Introduction

A python program aims to minimize a nonlinear cost function f(x,y) given two nonlinear constrains g1(x,y) and g2(x,y), where g1,2(x,y) < 0.

## Requirments

```python
pip install numpy
pip install scipy
pip install matplotlib
```

## Usage

* Run optimize.py file

```python
pytohn optimize.py
```

* Enter cost function equation.
* Enter the two constrains g1(x,y) and g2(x,y) equations.
* Enter the intial point value of (x,y).

* Returns
    * A plot window apears of f(x,y), g1(x,y), and g2(x,y) vs iteration index.
    * The final minimized value of cost function, g1(x,y), g2(x,y), and x will be printed.

## Important Dependencies

* Equations must be written within x and y variables.