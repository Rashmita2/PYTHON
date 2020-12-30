#appending items to the list
choice = "-"
computer_parts = [] #empty list
while choice != '0':
    if choice in "12345":
        print("Adding {}".format(choice))
        if choice == '1':
            computer_parts.append("computer")
        elif choice == '2':
            computer_parts.append("mouse")
        elif choice == '3':
            computer_parts.append("keyboard")

    else:
        print('Please add the option form the list')
        print('1: computer')
        print('2: monitor');
        print('3: keyboard')
        print('4: mouse')
        print('5: mouse pad')

    choice = input()

print(computer_parts)