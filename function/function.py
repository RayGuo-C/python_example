# To define a function will make the program easier
# note the usage of reture

def message(name, age):
    print(name + ': age is ' + age)

message('ray','24')
message('Meiye','24')

def cube(num):
    return num * num * num

result = cube(4)
print(result)