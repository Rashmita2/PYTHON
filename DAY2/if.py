is_male = True
if is_male:
    print("You are male")
else:
    print('You are female')

def find_max(num1,num2, num3):
    if num1 >= num2 and num1 >= num3:
        print("Num1 is greater than num2 and num3");
    elif num2 >= num1 and num2 >= num3:
        print("Num2 is greater than num2 and num3");
    else:
        print("Num3 us greater");

find_max(4,7,3);
