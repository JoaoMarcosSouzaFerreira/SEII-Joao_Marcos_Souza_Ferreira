import numpy as np

a = np.array([[1,2,6], [3,4,8]])
print(a)
print(a.shape)
print(a[0][0])
print(a.T)

b = np.array([[1,2],[3,4]])
print(np.linalg.det(b)) 
print(np.diag(b))  
