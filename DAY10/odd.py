
max_num = int(input("Enter max number: "))

odd_numbers = []

for i in range(max_num):
    if i%2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ",odd_numbers)