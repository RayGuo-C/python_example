'''
https://www.youtube.com/watch?v=V0D2mhVt7NE
'''

'''
1. calculate the sum
'''
a = [1, 2, 3, 4]
b = [10,11,12,12]
c = a+b
print("don't use numpy",'c=a+b:',c)

output = []
for item1, item2 in zip(a,b):
	output.append(item1 + item2)
print("don't use numpy to get the value c=a+b:",output)

g = list(range(10000))
print('sum(g)', sum(g))


'''
2. directly calculate through matrix
'''
# sum
import numpy as np 
g_array = np.array(g)
print(sum(g_array))

c = np.array([1,2,2,3])
d = np.array([1,2,3,2])
l = c+d
print('l',l)

# matrix transpose
print('matrix transpose')
a = np.array([[1,2,3],[1,2,2]])
b = np.array([[1,2,3],])
c = np.array([1,2,3])
a_2 = a.transpose()
b_2 = b.transpose(1,0)
c_2 = c.transpose()
print(a_2)
print(b_2)
print(c_2)
print(a_2.ndim)
print(b_2.ndim)
print(c_2.ndim)

# matrix multiply
print('matrix multiply')
B = b.transpose() 
print(np.dot(B,b))
print(np.multiply(b,b))
l1 = np.exp(c)
l2 = np.sin(c)
l3 = np.log(c)
print('l1,l2,l3',l1, l2, l3)

'''
3. setting array element
'''
e = np.array([1,2,3,1],dtype='int64')
c = np.array([[0,7,4], [3,4,5]])
print('setting array element')
print('ndim',c.ndim)
print('shape',c.shape)
print('dtype',c.dtype)
print('size',c.size)
print('type',type(c))
print('get the value by index',c[0,1])

'''
4. array slicing
'''
print('array slicing')
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
a means the third dimension = 
b means the cow  = aixs0
c means the collum = axis-1
'''
# 2D array
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
for i in range(a.shape[0]):
	print('row:'+str(i),a[i,:])
for i in range(a.shape[1]):
	print('collum:'+str(i),a[:,i])
# 3D arrat
b = np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[1,1,1,1],[2,2,2,2],[3,3,3,3]]])
for i in range(b.shape[0]):
	print('third_dimension:'+str(i),b[i,:,:])
for i in range(b.shape[1]):
	print('row:'+str(i),b[:,i,:])
for i in range(b.shape[2]):
	print('collum:'+str(i),b[:,:,i])
for i in range(b.shape[0]):
	for j in range(b.shape[1]):
		print('each row'+str(i)+str(j),b[i,j,:])
# creat array to restore the value



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

# 8. get serios numbers
print(np.linspace(0,1,11))
print(np.arange(0,1,0.1))