#writing in a file
city = ["Texas", "Oklahoma", "NewYork", "Colorado"]

with open('data2.txt', 'w') as city_file:
    for index in city:
        print(index, file=city_file)