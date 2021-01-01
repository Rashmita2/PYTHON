#using break statement
x = int(input('How many candies do you want? '))
i = 1
av_candies = 50
while i <=x:
    if i >= av_candies:
        print("we are out of candies")
        break

    print("candy")
    i+=1