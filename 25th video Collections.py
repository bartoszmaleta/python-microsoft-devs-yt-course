from array import array         # used later

names = ['Bartosz', 'Magda']
print(names)

scores = []
scores.append(98)   # Add new item to the end
scores.append(85)
print(scores)
print(scores[1])        # collections are zero-indexed


points = array('d')         # d stands for digits
points.append(44)
points.append(12)
print(points)
print(points[1])

# Arrays:
#     - designed for simple types such as numbers
#     - must all be the same type

# Lists:
#     - store anything
#     - store any type

last_names = ['Maleta', 'Huget']
print(len(last_names))     # get the number of items in last_names
last_names.insert(0, 'Krawiec')  # Insert before index
print(last_names)
last_names.sort()
print(last_names)

# _________________________
# Retrieving ranges

second_names = ['Messi', 'Ronaldo', 'Rooney']
footballers = second_names[0:2] # will get the first two items!
# first number is starting index, second number is number of
# items to retrieve

print(second_names)
print(footballers)

# ___________________________
# Dictionaries

person = {'first': 'Jakub'}
person['last'] = 'Maleta'
print(person)
print(person['first'])

# Dictionaries:
#     - key/value pairs
#     - storage order not guaranteed

# Lists
#     - zero-based index
#     - storage order guaranteed