'''
Problem: Create a dictionary which associates author names to lists of titles.
Write a program which asks for an author's name, and prints as a string the list 
of books by that author. 
Stretch goal: return results in alphabetical order.
'''

books = {
    "margaret atwood":["The Handmaid's Tale", "The Blind Assassin"],
    "j.r.r. tolkien":["The Hobbit", "The Silmarillion", "The Lord of The Rings"],
    "roald dahl":["Matilda", "James and The Giant Peach", "Charlie and The Chocolate Factory"]
    }

name = input("Enter author name: ")
results = books.get(name.lower(), [])
results.sort()
print(f"Books by {name}:", ', '.join(results))