import numpy as np

column,row = 16,16
nbBombe= 40
a=np.zeros((column*row),dtype=object)

a[:nbBombe]="b"
np.random.shuffle(a)
a= np.reshape(a,(column,row))
print(a)

