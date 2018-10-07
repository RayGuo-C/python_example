# power function

num_base = 2

def result(num_power):
    result = num_base
    index = 1
    while index < num_power:
        index = index + 1
        result = result * num_base
    print(result)

  #  return result

print(result(2))

