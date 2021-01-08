import random
digits = list(range(10))
random.shuffle(digits)
print(digits[:3])

guess = input("What is your guess? ")
print(guess)
if guess == digits:
    print('Match')
else:
    print('Didn\'t match')