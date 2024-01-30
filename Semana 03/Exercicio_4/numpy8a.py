import numpy as np 

a = np.array([[1,2], [3,4], [5,6]])
print(a)
bool_idx = a > 2    
print(bool_idx)
print(a[bool_idx]) 
b = np.where(a>2, a, -1)
print(b)
c = np.array([10,19,30,41,50,61])
d = [1,3,5]
print(c[d]) 
