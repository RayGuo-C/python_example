
file = open('name_list.txt','w')
a = [
    [1,1,2,3],
    [2,2,3,4],
    [3,3,4,5]
]
for row in a:
    file.write(str(row))
    file.write('\n')

file.close()