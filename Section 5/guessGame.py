# This is a guess the number game
import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1,20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20')7

for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low')

    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break #This condition means the guess is correct

if guess == secretNumber:
    print('Good job, ' + name + ' you guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope, the number I was thinking of was ' + str(secretNumber))

print('You took ' + str(guessesTaken) + ' guesses')

