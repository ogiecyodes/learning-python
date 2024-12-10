import numpy as np
arr = np.array([1,2,3,4,5,6,7])# 1-D array
print(arr)
print(np.__version__)
print(arr.ndim)
#0-D array or Scalar
arr = np.array(32)
#2-D arrays
a = np.array([[1,2,3], [4,5,6]]) # 2 list of 1 dimension
#3-D arrays
b = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])# 2 list of 2 dimensions
print(a.ndim)
print(b.ndim)
