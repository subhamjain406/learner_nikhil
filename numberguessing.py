import random

print('lets play a game')
n = random.randint(1,99)
guess=int(input('enter any number between 1 to 99' ))
while n!= guess:
    print()
    if guess < n:
        print('the number is too low')
        guess = int(input('enter any number between 1 to 99'))
    elif n < guess:
        print ('the number is too high')
        guess = int(input('enter any number between 1 to 99'))
    else:

        break
print('u gussed it correct')


