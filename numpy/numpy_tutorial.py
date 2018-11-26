'''
https://www.youtube.com/watch?v=V0D2mhVt7NE
'''
'''
1. calculate the sum
'''
a = [1, 2, 3, 4]
b = [10,11,12,12]
c = a+b
print(c)

output = []
for item1, item2 in zip(a,b):
	output.append(item1 + item2)
print(output)

g = list(range(10000))
print(sum(g))


'''
2. directly calculate through matrix
'''
import numpy as np 
g_array = np.array(g)
print(sum(g_array))

print(a)

c = np.array([1,2,2,3])
d = np.array([1,2,3,2])
l = c+d
print(l)

l1 = np.exp(c)
l2 = np.sin(c)
l3 = np.log(c)
print(l1, l2, l3)

'''
3. setting array element
'''
e = np.array([1,2,3,1],dtype='int64')
c = np.array([[0,7,4],
	          [3,4,5]])
print('setting array element')
print(c.ndim)
print(c.shape)
print(c.dtype)
print(c.size)
print(type(c))
print(c[0,1])

'''
4. array slicing
'''
print(c[:,::2])
d = np.arange(9).reshape(3,3)
print(d)

'''
5. indexing by position and booleans
'''
a_1 = np.array([3,-1,-2,-4,5,4])
index = [1,3]
print(a_1[index])
negative = a_1 < 0
print(a_1[negative])
print(a_1[a_1>0])
c = np.array([10,1,20,23,23,12])
d = np.array([2,3,43,23,12,23])
print(a_1[c>d])
e = np.array([0,1,0,1,1,0],dtype=bool)
print(a_1[e])

a_2 = np.array([[0,1,2,3,4,3],
	            [2,3,1,2,3,2]])
print(a_2[1,negative])

'''
6. multi_dimensional arrays
(a,b,c)
a means wide of cubic = 
b means high of cubic = aixs0
c means length of cubic = axis-1
'''
print('3D matrix')
a_3 = np.zeros((2,2,3))
print(a_3)
'''
7. computation with arrays
Rule 1: Operation between multiple array  objects are first checked for proper shape match
Rule 2: Mathematical operations(+ - / * exp, log,...) apply element by element, on the calues
'''
print('multi_dimensional arrays')
print(sum(a_1))
print(sum(a_2)) 
print('calcualte the sum of one axis')
print(a_2.sum(axis=0))
print(np.sum(a_2,axis=0))
print(a_2.sum(axis=-1))
print('calcualte the mean of one axis')
print(a_2.mean(axis=-1))
print('find the minimus value of one axis')
print(a_2.min(axis=0))
print(np.min(a_2,axis=0))
print('find the index of minimum value one axis')
print(a_2.argmin(axis=0))
print(np.argmin(a_2,axis=0))