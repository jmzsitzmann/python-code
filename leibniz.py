def calcPi(iterations):
    pi4 = 0.0
    n = 1.0
    r = 3.0
    for i in range(iterations):
        pi4 = pi4 + (1.0 / n) - (1.0 / r)
    
        n = n + 4
        r = r + 4
    pi = pi4 * 4.0
    return pi
print('The approximate value of pi is: ', calcPi(10000))
      
    