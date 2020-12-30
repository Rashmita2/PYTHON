answer = 5
ans = int(answer)
guess = int(input('Enter your guess between 1 and 10: '))
if guess < answer:
     print("Guess is low")
elif guess > answer:
    print("Guess is high")
else:
    print("Yeah! You won")

