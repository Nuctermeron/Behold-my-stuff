import random

computerNumber = random.randint(1,30)
print ('I am thinking about number between 1 and 30. Can you guess which one?')
print ('You have only 5 tries!')
guessNumber = 5


#challenge
for guessCount in range(1,31):
    print('Take a guess...')
    guess = int(input())
    
#Guess
    if guess < computerNumber:
        guessNumber = guessNumber - 1
        print('Your guess is too low, only ' + str(guessNumber) + ' tries remains')
    elif guess > computerNumber:
        guessNumber = guessNumber - 1
        print('Your guess is too high, only ' + str(guessNumber) + ' tries remains')
    else:
        break
    
if guess == computerNumber:
    print('Well done! That is my number')
else:
    print('You have failed, I was thinking about ' + str(computerNumber))    