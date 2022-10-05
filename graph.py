import numpy as np
from values import Values
from syssolver import Solver
import matplotlib.pyplot as plt

def Graph(filename, n, xlabel = '', ylabel = ''):
    t = np.arange(Values(filename)[0][0], Values(filename)[0][-1], 0.2)
    p = 0
    i = 0
    while i <= n: p = p + Solver(filename, n)[i]*(t**i); i = i + 1
    plt.plot(Values(filename)[0], Values(filename)[1], 'bo', label="Data")
    if n == 1:
        plt.plot(t, p, 'k', label="First degree polynomial")
    if n == 2:
        plt.plot(t, p, 'k', label="Second degree polynomial")
    if n == 3:
        plt.plot(t, p, 'k', label="Third degree polynomial")
    else:
        plt.plot(t, p, 'k', label="{}th degree polynomial".format(n))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.savefig('{}th degree'.format(n))
    





