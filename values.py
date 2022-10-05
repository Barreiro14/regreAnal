import numpy as np



def Values(fileName):
    file = open("{}".format(fileName))
    x = []
    E = []
    pdos = []
    for line in file:
        #print(line)
        x.append(line.split())
        #y = x.split()


    x.pop(0)
    i = 0
    j = 0
    #print(x[0])

    while i < len(x):
        while j < 2:
            if j == 0:
                E.append(x[i][j])
            else:
                pdos.append(x[i][j])
            j = j + 1
        j = 0
        i = i + 1

    E = np.array(E)
    E = E.astype(np.float)

    pdos = np.array(pdos)
    pdos = pdos.astype(np.float)
    return E, pdos
    #print("E (eV) es:", E)
    #print("pdos(E) es:", pdos)
    #print(type(E[0]))