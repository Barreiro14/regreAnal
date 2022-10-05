from values import Values

def xValues(filename, n):
    Values(filename)
    x = 0
    for element in Values(filename)[0]:
        x = x + element**n
    return x

def xyValues(filename, n):
    Values(filename)
    xy = 0
    i = 0
    while i < len(Values(filename)[1]):
        xy = xy + Values(filename)[1][i]*(Values(filename)[0][i]**n)
        i = i + 1

    return xy

  
