sent = "Computer Science and Technology"
#sorts capital letter on first
letter = sorted(sent)
print(letter)
#sort capital letter alphabetically
letter1 = sorted(sent, key= str.casefold)
print(letter1)

computer = ['mouse','Keyboard', 'Monitor', 'speaker']
computer.sort(key=str.casefold)
print(computer)