'''
Input: mark
Output: distinction if > 85, pass if 65 <= mark <= 85, fail otherwise
'''

mark = int(input("Enter a mark: "))

# input validation: ensuring 0 <= mark <= 100
while mark > 100 or mark < 0:
    print("Mark must be between 0 and 100")
    mark = int(input("Enter a mark: "))

# with elif
if mark > 85:
    print("Distinction")
elif mark >= 65:
    print("Pass")
else:
    print("Fail")

# Without elif - block
if mark > 85:
    print("Distinction")
else:
    if mark >= 65:
        print("Pass")
    else:
        print("Fail")

# Without elif - inline
print("Distinction" if mark > 85 else \
    ("Pass" if mark >= 65 else \
    "Fail"))