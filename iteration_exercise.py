'''
Problem: Write a program which takes in 5 names, and prints each name,
followed by 'is awesome!'.
'''

# while
# i = 0
# while i < 5:
#     name = input("Enter name: ")
#     print(name, "is awesome!")
#     i += 1

# for
# for i in range(5):
#     name = input("Enter name: ")
#     print(name, "is awesome!")

# both
names = []
while len(names) < 5:
    names.append(input("Enter name: "))

for name in names:
    print(name, "is awesome!")