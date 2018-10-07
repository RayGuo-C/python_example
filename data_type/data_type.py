

print('hello world')

character_name = 'Ray'
character_age = 24
character_age_str = '24'

# We need to use plus signal (+) to connect two character strings
# Note the difference to show the string and int data types
print('my name is ' + character_name + ',')
print('and my age is ', character_age )
print(character_age)
print('my age is '+ character_age_str )
print('my age is ' + str(character_age))

# The difference between single quote and double quote
print('I\'m ' + character_name)
print("I 'm " + character_name)
print(' I am studying "python"')
print(" I am studying \"python\"")
print('I am studying \n "python"')
print(''' I am studying 
                        "python"''')

# Basic knowledge of string
print(character_name.upper()) # using the build in functions
print(character_name.upper().isupper())
print(len(character_name)) # the numeber of character string
print(character_name[0]) # counting from zero
print(character_name.index('R')) # get the index of the letter
print(character_name.replace('AY','ay'))

# print the message form users
name = input('please input your name')
print('hello' + name + '! Welcome you enter into this new world.')