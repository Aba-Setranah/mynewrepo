import random

randomnum = random.randint(1,101)
print(randomnum)
while True:
    guess = input('guess selected random number between 0 and 100: ')
    if int(guess) == randomnum :
        print('just right')
        break
    elif int(guess) < randomnum :
        print('too low')
    elif int(guess) > randomnum :
        print('too high')
    else: print('invalid')
