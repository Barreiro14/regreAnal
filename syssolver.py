import numpy as np
from values import Values
from xysums import xValues, xyValues

def Solver(filename, n): #el orden es el order del polinomio de Taylor a evaluar
    w = np.zeros((n + 1, n + 1))
    S = np.zeros(n + 1)
    i = 0
    I = 0
    while i < len(w):
        j = 0
        while j < len(w[0]):
            if i == 0 and j == 0:
                w[i, j] = len(Values(filename)[0]) #Cantidad de datos obtenidos
            else:
                w[i, j] = xValues(filename, i + j)
            j = j + 1
        i = i + 1
    i = 0
    while i < len(S):
        S[i] = xyValues(filename, i)
        i = i + 1
    i = 0
    ai = np.linalg.solve(w, S)
    return ai


    
'''
Solver(3)
'''