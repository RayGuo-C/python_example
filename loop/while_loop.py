# guess the word
# count the number of guess, once over three times, the game over

secret_word = 'Ray'
guess = ''
count = 0
gameison = True

while guess != secret_word and gameison:
    guess = input('re-input the word: ',)
    count = count + 1
    if count >= 3:
        print('game over')
        gameison = not(gameison)

if guess == secret_word:
    print('you win')

# while-while loop
i = 0
while i < 10:
	j = 1 # otherwise the code cannot be implemented since the j = 11
	while j < 11:
	 	print(i, j)
	 	j+=1
	i+=1