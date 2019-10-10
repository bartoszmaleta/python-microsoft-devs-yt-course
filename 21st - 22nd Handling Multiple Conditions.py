# province = input('What province are you from? ')

# province2 = input('What province are you from? ')


# if province == 'Alberta':
#     tax = 0.05
# elif province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15

# if province == 'Alberta' or province == 'Nunavut':
#     tax = 0.05
# elif province == 'Ontario':
#     tax = 0.13
# else:
#     tax = 0.15


# if province2 in ('malopolskie', 'slaskie', 'wielkoposlie'):
#     tax = 0.05
# elif province2 == 'pomorskie':
#     tax = 0.13
# else:
#     tax = 0.15

# _________________ good option?

# if country.lower == 'polska':
#     province2 = input('What province are you from? ')
#     if province2 in ('malopolskie2', 'slaskie2', 'wielkoposlie2'):
#         tax = 0.05
#     elif province2 == 'pomorskie2':
#         tax = 0.13
#     else:
#         tax = 0.15
# else:
#     tax = 0.0
# print(tax)

# __________________________________ best option:

country = input('What country are you from? ')

if country.lower() == 'polska':
    province = input('What province are you from? ')
    if province in ('malopolskie2', 'slaskie2', 'wielkoposlie2'):
        tax = 0.05
    elif province == 'pomorskie2':
        tax = 0.13
    else:
        tax = 0.15
else:
    tax = 0.0
print(tax)