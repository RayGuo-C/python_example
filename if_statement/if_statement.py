# if_statement syntax

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        print('the maximum is ', num1)
    elif num2 >= num1 and num2 >= num3:
        print('the maximum is ', num2)
    else:
        print('the maximum is ', num3)

max_num(3,4,2)


