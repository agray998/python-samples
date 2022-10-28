# Definitions:
# Collection: Data type that holds several values
# Mutable: Able to be changed
# Ordered: Retains order of elements, accessible via indices

# Lists: ordered, mutable
fruits = ["Apple", "Cherry", "Banana", "Apricot", "Orange", "Apple"]
# Adding elements: append, insert, extend
fruits.append("Pear") # Adds to end of list
fruits.insert(2, "Strawberry") # Adds at index specified by first argument
fruits.extend(["Pineapple", "Raspberry", "Plum"]) # Adds each element in turn to end of original list
# Removing elements: remove, pop, del
fruits.remove("Apple") # Removes given value (first occurence if more than one)
fruits.pop(2) # Removes, and returns, element at given index
del fruits[0] # Removes element at index, does not return
# Updating elements: Assigning new value to index
fruits[2] = "Grapefruit"
# Sorting Lists
fruits.sort() # Sort method sorts list in place
print(sorted(fruits)) # Sorted function returns sorted list as new list, leaves original unchanged


# Tuples: ordered, immutable
tuple_a = [1, 2, 3], [4, 5, 6], [7, 8, 9]
tuple_a[1][1] = 0
print(tuple_a)

# Dictionaries: ordered(ish), mutable
cap_cities = {"UK":"London", "France":"Paris", "Belgium":"Brussels"} # dict(key=value,...)
# print(cap_cities["Germany"])
print(cap_cities.get("Germany", "Not there"))
# cap_cities["Italy"] = "Rome"
cap_cities.update(Italy="Rome")
print(cap_cities.pop("Belgium"))
del cap_cities["UK"]
print(cap_cities)

# Sets: unordered, mutable
# Note: sets will discard duplicate values, and can only store objects of immutable types
empty_set = set()
set_a = {2, 3, 1, 1, 2, 3, 3, 2, 1}
set_a.discard(4) # discard method does nothing if value is not an element of the set
print(set_a)
