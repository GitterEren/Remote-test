import random
secret=random.randint(1,9)
guess=' '
trial=0
while guess != secret:
    guess=int(input('Please enter a number between 1-9: '))
    trial+=1
    if guess==secret:
        print('You have won')
        break
    if trial ==3:
           print('You have failed')
           break
