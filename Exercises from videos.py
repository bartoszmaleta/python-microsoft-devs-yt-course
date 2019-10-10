print('Hello world')
print()
print('Did you see that blank line?')
print('Blank line \nin the middle of string') 
# ctrl + k + c  ----> comment line
# ctrl + k + u -----> uncomment line

first_name = 'Bartosz'
last_name = 'Maleta'
print(first_name + last_name)
print('Hello ' + first_name + ' ' + last_name)

sentence = 'The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))


# first_name2 = input('What is your first name? ')  ----> commented, because wanted to continue with more examples
# last_name2 = input('What is your last name? ')
# print('Hello ' + first_name2.capitalize() + ' ' + last_name2.capitalize())
# ___________________________________________


first_name3 = 'Bartosz'
last_name3 = 'Maleta'

# first_name3 = input('Please enter your first name')
# last_name3 = input('Please enter your last name')

print(first_name3 + last_name3)
print('Hello, ' + first_name3 + ' ' + last_name3)

print(last_name3.upper())


first_name4 = input('Please enter your first name: ')
last_name4 = input('Please enter your last name: ')

output = 'Hello, ' + first_name4 + ' ' + last_name4
output2 = 'Hello, {} {}'.format(first_name4, last_name4)
output3 = 'Hello, {0} {1}'.format(first_name4, last_name4)

# Only available in Python 3:
output4 = f'Hello, {first_name4} {last_name4}' # f ---> format

print(output)
print(output2)
print(output3)
print(output4)
