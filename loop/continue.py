#3. Continue: jump the if condition in the inner loop
for i in range(5):
	for j in range(4):
		if j == 2:
			continue
		print(i,j)

#4. continue the while-statement 
a = 10
while a > 1:
	a -= 1
	if a == 5:
		continue
	print(a)
