import numpy as np
import time
import sys

arr_1 = np.array([[1, 3], [2, 4]])
arr_2 = np.array([[5, 7], [6, 8]])
transpose_mat = arr_1.T
dot_product = np.dot(arr_1, arr_2)
print("Transpose of arr_1 is : ", transpose_mat)
print("Dot product of arr_1 and arr_2 is : ", dot_product)
dot_product_2 = arr_1.dot(arr_2)
print(dot_product_2)
# arr_1 = np.arange(16)
# print(arr_1)
# reshape_arr = np.reshape(arr_1, (4, 4))
# print(reshape_arr)
# reshape_arr_2 = arr_1.reshape(4, 4)
# print(reshape_arr_2)
# print(reshape_arr.sum())
# print(reshape_arr.mean())
# print(reshape_arr.min())
# print(reshape_arr.max())
# ls = list(range(10000))
# bf_time = time.time()
# sum([x * 2 for x in ls])
# af_time = time.time()
# print(sys.getsizeof(ls))
# print("Default python time taken: ", af_time - bf_time)

# np_arr = np.arange(1000)
# np_bf_time = time.time()
# np.sum(np_arr * 2)
# np_af_time = time.time()
# print(np_arr.nbytes)
# print("Numpy time taken: ", np_af_time - np_bf_time)

