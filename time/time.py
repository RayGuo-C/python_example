import time
import numpy as np 
import random
a = np.random.rand(10000)
b = np.random.rand(10000)
tic = time.time()
c = np.dot(a,b)
toc = time.time()
print('the time need to calculate with vectorization', toc-tic)

a = []
tic = time.time()
for i in range(10000):
	for j in range(10000):
		a = i*j
toc = time.time()
print('the time need to calculate without vectorization', toc-tic)
