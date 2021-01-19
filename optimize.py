import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

class Optimizer:
    ''' 
    This class for minimizing a nonlinear cost function, given two nonlinear constrains.
    
    Parameters:
        costFunction_str (str): cost function equation f(x,y).
        gOne_str (str): first constrain function equaiton.
        gTwo_str (str): second constrain function equation.
        x0 (float): initial point value x.
        y0 (float): initial point value of y.
        eps (float): episolon value.
    '''
    def __init__(self, costFunction_str, gOne_str, gTwo_str, x0, y0, eps=0.000001):
        self.costFunction_str = costFunction_str
        self.gOne_str = gOne_str
        self.gTwo_str = gTwo_str
        self.x0 = np.array([x0, y0])
        self.eps = eps
        self.cons = ({'type': 'ineq', 'fun': self.constrain})
        self.cost_values = []
        self.g1_values = []
        self.g2_values = []
        self.res = []

    def costFunction(self, x):
        return eval(self.costFunction_str, {'x':x[0], 'y':x[1]})

    def gOne(self, x):
        return eval(self.gOne_str, {'x':x[0], 'y':x[1]})

    def gTwo(self, x):
        return eval(self.gTwo_str, {'x':x[0], 'y':x[1]})

    def constrain(self, x):
        return self.eps - self.gOne(x), self.eps - self.gTwo(x)

    def callbackF(self, Xi):
        self.cost_values.append(self.costFunction(Xi))
        self.g1_values.append(self.gOne(Xi))
        self.g2_values.append(self.gTwo(Xi))

    def optimizing(self):
        self.res = minimize(self.costFunction, self.x0, method='SLSQP',
                            constraints=self.cons,
                            callback=self.callbackF)

    def plot(self):
        iter_range = range(len(self.cost_values))
        plt.figure(figsize=(8,8))
        plt.plot(iter_range, self.cost_values, label='Cost Function')
        plt.plot(iter_range, self.g1_values, label='g1')
        plt.plot(iter_range, self.g2_values, label='g2')
        plt.legend(loc='upper right')
        plt.title('f(x, y) and g1,2(x, y) vs iteration index.')
        plt.savefig("plot.jpg")
        plt.show()

if __name__ == "__main__":
    costFunction_str = input("Please enter the cost function: ")
    gOne_str = input("Please enter the first constrain function g1: ")
    gTwo_str = input("Please enter the second constrain function g2: ")
    x0 = float(input("Please enter the initial value of x: "))
    y0 = float(input("Please enter the initial value of y: "))

    optimizer = Optimizer(costFunction_str, gOne_str, gTwo_str, x0, y0)
    optimizer.optimizing()
    
    print("Final mimimized cost function value: ", optimizer.res.fun)
    print("Final value of x and y: ", optimizer.res.x)
    print("Final g1 constrain value: ", optimizer.gOne(optimizer.res.x))
    print("Final g2 constrain value: ", optimizer.gTwo(optimizer.res.x))

    optimizer.plot()