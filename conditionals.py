condition = True
condition_2 = True
# truthiness
# Collections: empty = False, non-empty = True
# Numerical: Zero = False, non-zero = True
# Boolean expressions:
# True/False, including variables
# Comparison operators: <, >, <=, >=, ==, !=, in, is
# Function call that returns bool
time = input("Enter time: ")

if time < "12:00": # predicate
    print("It's the morning") # code to execute - consequent
# elif time == "12:00":
#     print("It's noon")
else:
    if time == "12:00":
        print("It's noon")
    else:
        print("It's the afternoon") # alternate

# [consequent] if [predicate] else [alternate]

# print("It's the morning" if time < "12:00"\
#     else ("It's noon" if time == "12:00"\
#     else "It's the afternoon"))