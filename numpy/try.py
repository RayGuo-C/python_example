import random
'''
1. random the number between 1 and 10
'''
result_value = random.uniform(1,10)


'''
2. random choose the subject based on weights
'''
color = 'red', 'blue', 'black'
result_color = random.choices(color,weights=[10,10,2],k=22)

'''
3.random choose the 
'''
number = list(range(1,50)) 
result_number = random.shuffle(number)
hand = random.sample(number,k=5)

