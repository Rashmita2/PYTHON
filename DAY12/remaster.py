#dict has a key-value pair

vehicles = {"Honda": 2017,
            "BMW":2020,
            "Ford": 2010
}
my_car = vehicles['BMW']
print(my_car)
#second method
my_car1 = vehicles.get('BMW')
print(my_car1)
#if the key doesn't exist, it returns None

for key in vehicles:
    print(key, vehicles[key])

print()
vehicles["Tesla"] = 2019
#to seperate from a seperator
for key,value in vehicles.items():
    print(key, value, sep=", ")

