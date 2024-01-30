import numpy as np 

data = np.genfromtxt('spambase.csv',delimiter = ",", dtype=np.float32)
print(data.shape)
