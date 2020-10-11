import random
secret = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
for guessesTaken in range(1, 5):
    print('Take a guess.')
    guess = int(input())
    if guess < secret:
        print('Your guess is too low.')
    elif guess > secret:
        print('Your guess is too high.')
    else:
        break
if guess == secret:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses')
else:
    print('Nope. The number I was thinking of was ' + str(secret))