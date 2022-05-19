import random

def number_picker():
    value=random.randint(1,100)
    return value

def guess_check(guess):
    if guess== num:
        print(f'You win! The answer was {num}')
        return True
    elif guess>num:
        print('Too high.\nGuess again.')
        return False
    else:
        print('Too low.\nGuess again.')
        return False


print('Welcome to the Number Guessing Game')
print('I\'m thinking of a number between 1 and 100.')
check=input('Choose a difficulty. Type \'easy\' or \'hard\': ' ).lower()
if check=='easy':
    attempts=10
else:
    atempts=5

num=number_picker()
print(f'You have {attempts} attempts to guess the number.')
while attempts>0:
    guess=int(input('Make a guess: '))
    check=guess_check(guess)
    attempts-=1
    if check:
        break
    else:
        print(f'You have {attempts} attempts remaining to guess the number.')

