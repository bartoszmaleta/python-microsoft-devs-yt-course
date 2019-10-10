# First Loop

for names in ['Bartosz', 'Magda']:
    print(names)

for index in range(0, 5):
    print(index)

# _____________________
# Second Loop


footballers = ['Messi', 'Ronaldo']
index = 0

while index < len(footballers):
    print(footballers[index])
    # now, you have change the condition ---> index!
    index = index + 1

# __________________________

print()
singers = ['Jakub', 'Amelia']
for name in singers:
    print(name)

print()

# ________________in while loop its gonna look like this:
index = 0
while index < len(singers):
    print(singers[index])
    index = index + 1

print()
