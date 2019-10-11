import datetime

# print timestamps to see how long sections of take to run

name1 = 'Bartosz'
print('task completed')
print(datetime.datetime.now())
print()

for x in range(0, 10):
    print(x)
print('task completed')
print(datetime.datetime.now())
print()


# ____________________ Function:

# print the current time
def print_time():
    print('task completed')
    print(datetime.datetime.now())
    # to use print(datetime.now()) write at the top:
    # from datetime import datetime!!!!
    print()


second_name = 'Maleta'
print_time()
for x in range(0, 10):
    print(x)
print_time()


# to have a specific string or parameter:
def print_time2(task_name):
    print(task_name)
    print(datetime.datetime.now())
    print()


third_name = 'Magda'
print_time2('third name assigned')

for x in range(0, 10):
    print(x)
    print_time2('loop completed')


# 1) version

first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1]
last_name = input('Enter your last name: ')
last_name_initial = last_name[0:1]


print(first_name_initial.upper() + last_name_initial.upper())

# ____________________ or
# 2) version


def get_initial(name):
    initial = name[0:1].upper()
    return initial


first_name2 = input('Enter your first name:')
first_name2_initial = get_initial(first_name2)

last_name2 = input('Enter your last name: ')
last_name2_initial = get_initial(last_name2)

print('Your initials are: ' + first_name2_initial + last_name2_initial)


# _______________ or
def get_initial2(name):
    initial = name[0:1].upper()
    return initial


first_name3 = input("your firist name: ")
last_name3 = input("your last name: ")


print('Your initials are: ' + get_initial2(first_name3) + get_initial2(last_name3))
