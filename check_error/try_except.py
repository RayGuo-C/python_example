# this function is to tell us the error position, and the error will not cause program break

try:
    answer = 10/0
except ZeroDivisionError as err:
    print(err)

a = 2
print(a)