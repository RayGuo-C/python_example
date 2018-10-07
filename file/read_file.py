
file = open('name_list.txt','r')

print(file.readlines())
# print(file.read())
print(file.readable())

file.close()