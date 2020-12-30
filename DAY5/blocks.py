for i in range(1,5):
    print('No. {} squared is {} and cubed is {:4}'.format(i, i**2, i**3))
print("*" * 20)

name = input('Please enter your name? ')
age = input('How old are you, {}? '.format(name))
age1 = int(age)
if age1 >= 18 and age1 < 99:
    print('You can vote. ')
elif age1 == 800:
    print('You cannot vote')
else:
    print('Cannot vote')
