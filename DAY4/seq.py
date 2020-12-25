#Strings replacement
str1 = "he's "
str2 = "probably "
str3 = "pining "
str4 = "for the "
str5 = "fjords "
print(str1+str2+str3+str4+str5)
print('hello ' * 5*4)

today = "friday"
print("day" in today )

age = 79
print("my age is " + str(age))
print("my age is {}".format(age))
print(f'my age is {age}')

#string formating

for i in range(1,13):
    print("No. {} square is {} and cube is {}".format(i, i**2, i**3))
