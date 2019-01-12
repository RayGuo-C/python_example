# The break and continue statement can terminate the current iteration or even the whole loop without checking the test expression
#1. break terminate the inner loop
'''
for i in range(5):
	for j in range(4):
		if j > 2:
			break
		print(i,j)
'''
#2.



'''
 for midlineCoord_r in midlineCoord_reshape:
			# make sure each sphere don't collip with each other
			  
			    elif distance(midlineCoord_r,vecPosition) <= (sphereR[0] + radius):
			    	break	 	

# break the while-statement 
a = 10
while a > 1:
	a -= 1
	if a == 5:
		break
	print(a)

'''