# Iteration
# repeatedly execute same code until stop condition

# while some condition is true
i = 0
while i <= 10:
    print(i)
    i += 1

# While loops commonly used for input validation, event loops

# for every object in iterable
fruits = ["apple", "pear", "cherry", "banana"]
for index, fruit in enumerate(fruits): # enumerate(list) returns iterator of tuples in the format (index, list[index])
    print("The", f"{index}'th fruit is", fruit.capitalize())

for i in range(0, 11, 1): # for loop over numeric range
    print(i)

cap_cities = {"UK":"London", "France":"Paris", "Italy":"Rome"}
for country, capital in cap_cities.items():
    print("Capital of", country, "is", capital)

# comprehensions
cap_fruits = [fruit.capitalize() if len(fruit) == 6 else fruit for fruit in fruits]
new_cap_cities = {capital:country for country, capital in cap_cities.items()} # example comprehension for inverting a dictionary
print(new_cap_cities)