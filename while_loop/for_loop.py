
friends = ['Juby','Bob','Tim',(1,2),('you','me')]
for friend in friends:
    print(friend)

# another method
for index in range(len(friends)):
    print(friends[index])

for i in range(1,5):
	print(i)
else:
	print('over')

# to track the different collow
a = [[[1,2,3,4],[2]],[[2,3,4,3],[2]],[[3,4,5,4],[2]]]
for i in a:
	print(i[0])