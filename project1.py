import random

print('Let\'s play hangman!')

# bank of random words
words = ['study', 'world', 'python', 'coder', 'confuse']

# initializing beginning values
playGame = True
join = ' '

#take input and start playing
while playGame == True:
    lives = 6
    wordFound = False
    word = words[random.randint(0,4)]
    solution = ['_' for i in word]
    print(join.join(solution))
    while wordFound == False:
        print('Lives Left: ', lives)
        guess = input('Guess a letter: ')
        if len(guess) != 1 or not (guess.isalpha()):
            print('Not a valid guess. Please enter a single letter.')
            continue
        if guess in word:
            index = word.find(guess)
            solution[index] = guess
            print (join.join(solution))
            print('Lives Left: ', lives)
        else:
            print("Letter not found!")
            print (join.join(solution))
            lives -= 1
            print('Lives Left: ', lives)
            continue
        if ''.join(solution) == word:
            wordFound = True
    print('Word guessed, You\'ve won!')
    playAgain = input('Play again? (yes/no)\n')
    if playAgain == 'no':
        playGame = False
