# same as before:


def get_initial2(name):
    initial = name[0:1].upper()
    return initial


first_name3 = input("Enter your firist name: ")
last_name3 = input("Enter your last name: ")


print('Your initials are: ' + get_initial2(first_name3) + get_initial2(last_name3))

# __________________


def get_iniial(name, force_uppercase=True):
    # force_uppercase and False added, to have a 
    # option to choose whether you want upperacse or not
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input('Enter your fist name: ')
first_name_initial = get_iniial(first_name, False)
# or
# first_name_initial = get_iniial(force_uppercase=False, \
#                                 name-first_name)
# dont have to be in order, if there is "="!!!!!

print('Your inital is: ' + first_name_initial)