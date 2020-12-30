#see if its exactly divisible by 8
numbers = [2,8,45,67,33]
for number in numbers:
    if number % 8 == 0:
        print('The numbers are not acceptable')
        break
    else:
        print('The number is {}'.format(number))
        