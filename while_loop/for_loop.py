
friends = ['Juby','Bob','Tim',(1,2),('you','me')]
for friend in friends:
    print(friend)

# another method
for index in range(len(friends)):
    print(friends[index])

# for - else: while finish codes in for-structure, then start to implement the else part
for i in range(1,5):
	for j in range(4):
		print(i,j)
else:
	print(i,j)
	print('over')

# to track the different collow
a = [[[1,2,3,4],[2]],[[2,3,4,3],[2]],[[3,4,5,4],[2]]]
for i in a:
	print(i[0])