import random
i = 0
highest = 10
answer = random.randint(1,41)
guess = 0
guess = int(input('Enter your guess: '))
while guess != answer:
    if guess == answer:
        print('The guess is correct')
        break
    else:
        print('No correct guess')
    i = i+1
