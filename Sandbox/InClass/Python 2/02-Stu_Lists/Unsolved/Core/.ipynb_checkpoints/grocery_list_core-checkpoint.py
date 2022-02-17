# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Sally
organize her grocery shopping list.
"""

# @TODO: Create a list of groceries
groceries = [
    'Water',
    'Butter',
    'Eggs',
    'Apples',
    'Cinnamon',
    'Sugar',
    'Milk'
]


# @TODO: Find the first two items on the list
first_two = groceries[:2]
print(first_two)


# @TODO: Find the last five items on the list
last_five = groceries[-5:]
print(last_five)


# @TODO: Find every other item on the list, starting from the second item
every_other = groceries[1::2]
print(every_other)


# @TODO: Add an element to the end of the list
groceries.append('flour')

print(groceries)


# @TODO: Changes a specified element within the list at the given index
groceries[groceries.index('Apples')] = 'gala apples'

print(groceries)


# @TODO: Calculate how many items you have in the list
print(len(groceries))



# Mike wants to find where gala apples is on his list. Find the index of gala apples.
print(groceries.index('gala apples'))
# Mike remembers that he already has sugar. Remove sugar from the grocery list.
groceries.remove('Sugar')
print(groceries)
# Mike decides that he has water at home. Remove water from the grocery list based on its index.
groceries.pop(groceries.index('Water'))
print(groceries)
# Mike decides to pick up the last item on his list, so remove the last item from the grocery list.
groceries.pop(-1)
print(groceries)
groceries.remove(groceries[-1])