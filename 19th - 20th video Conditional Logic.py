price = 1.3

if price >= 1.00:
    tax = .07
    print(tax)
else:
    tax = 0
    print(tax)

# or

if price >= 1.00:
    tax = .07
else:
    tax = 0
print(tax)

# ___________________________

# Comparing strings

country = 'CANADA'

if country == 'canada':         # Add .lower() to be okay!
    print('oh look a Canadian')
else:
    print('You are not from Canada')

country = 'CANADA'

if country.lower() == 'canada':
    print('oh look a Canadian')
else:
    print('You are not from Canada')

# ___________________________

price2 = input('How much did you pay? ')    # price2 because up the script is "price"

price2 = float(price2)

if price2 >= 1.00:
    tax = .07
    print('Tax rate is: ' + str(tax))
else:
    tax = 0
    print('Tax rate is: ' + str(tax))


# ___________________________

country2 = input('Enter the name of your home country: ')
if country2.lower() == 'canada':    # .lower() rozwiązuje sprawę!
    print('So you must like hockey!')
else:
    print('You are not from Canada')


