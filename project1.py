import random

print('Let\'s play hangman!')
print('If you would live to see a list of the letters you have already guessed, type in \'help\'.')
print('If you think you know the word and would like to guess, type in \'guess answer\'.')
# bank of random words
words = ['study', 'world', 'python', 'coder', 'confuse']

# initializing beginning values
playGame = True
join = ' '

# take input and start playing
while playGame == True:
    lives = 6
    usedLetters = []
    wordFound = False
    word = words[random.randint(0,4)]
    solution = ['_' for i in word]
    print(join.join(solution))
    print('Lives Left: ', lives)

    #loop in which a round is played, ends once game is won or lost
    while wordFound == False:
        #collect input
        userInput = input('Guess a letter: ')
        guess = userInput.lower()

        #if 'help' is entered display used letters
        if guess == 'help':
            print('You have already guessed:', ', '.join(usedLetters))
            continue
        #if 'guess answer' is entered allow the user to guess the word
        if guess == 'guess answer':
            guess = input('You can guess the word now: ').lower()
            if guess == word:
                print('That\'s right! You won!')
            else:
                print('Sorry that is incorrect')
            break
 
        # make sure guess is valid
        if len(guess) != 1 or not (guess.isalpha()):
            print('Not a valid guess. Please enter a single letter.')
            continue
        
        # check if letter has already been used
        if guess in usedLetters:
            print('You have already guessed this letter.')
            continue

        # store used letter in an array to keep track of
        usedLetters.append(guess)

        # check if guess is correct
        if guess in word:
            index = word.find(guess)
            solution[index] = guess
            print (join.join(solution))
            print('Lives Left: ', lives)
        else:
            print("Letter not found!")
            print (join.join(solution))
            lives -= 1
            if lives > 0:
                print('Lives Left: ', lives)
                continue
            else:
                print('Out of lives, game over!')
                break

        # check if game has been won
        if ''.join(solution) == word:
            wordFound = True
            print('Word guessed, you\'ve won!')
    
    
    # check if user wants to keep playing and validate options
    valid = False
    while (valid == False):
        play = input('Play again? (yes/no)\n')
        playAgain = play.lower()
        if playAgain == 'no':
            playGame = False
            valid = True
        elif playAgain == 'yes':
            print('New game!')
            valid = True
        else:
            print('Please enter a valid option.')
            continue
        
