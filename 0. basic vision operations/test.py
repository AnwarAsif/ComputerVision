import numpy as np 

A = np.array([[1,2,3],
              [4,5,6],
              [7,7,9]])
kernel = np.array([1/9 for i in range(9)]).reshape((3,3))

result = A * kernel 
print(result)