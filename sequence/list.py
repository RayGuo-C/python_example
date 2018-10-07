# list is one of the sequence, and each sequence has value and relevant index
# list can be changed as we want unlike tuple
# Create the list is to input comma-seperated data between square bracket

friends = ['kevin','Bob','Tim','Ray']
print(friends[3]) # we can get the result from start to end or end to start
print(friends[1:])
friends[-1] = 'Frack' # change the values of the vector
print(friends[2:])

# add the vector to the already existed vector
luck_number = [1, 2, 3, 4, 5]
friends.extend(luck_number)
print(friends)

# change the values for the vector
friends.append('Jim')
print(friends)

# insert the values for the vector
friends.insert(1, 'Ray')
print(friends)

# remove the valuse for the vector
friends.remove('Ray')
print(friends)

# delete the last values of vector
friends.pop()
print(friends)

# clear all the values of the vector
friends.clear()
print(friends)

# sort the number or character string of the vector
luck_number.sort()
friends.sort()
print(luck_number)
print(friends)
