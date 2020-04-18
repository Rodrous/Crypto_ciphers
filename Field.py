import numpy as np

def addition():
    field = int(input("enter GF:- "))
    n = 2 ** field

    result = [(i + j) % n for i in range(n) for j in range(n)]
    print(np.reshape(result, (4, 4)))

def mult():
    field = int(input("enter GF:- "))
    n = 2 ** field

    result = [(i * j) % n for i in range(n) for j in range(n)]
    print(np.reshape(result, (4, 4)))
