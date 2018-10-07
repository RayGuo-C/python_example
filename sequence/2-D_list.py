# the method to write a two dimensional array and print them
# Note that python read the array according to row sequence

twoD_list = [
    [1,2,3],
    [3,4,5],
    [1,2,5]
]
print(twoD_list)

for raw in twoD_list:
    print(raw)
    for num in raw:
        print(num)