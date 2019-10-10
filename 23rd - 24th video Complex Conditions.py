gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= .85:
    if lowest_grade >= .70:
        print('Well done')

# or (same thing), second one is recommended!


if gpa >= .85 and lowest_grade >= .70:
    print('Well done')

# _______________________________________

if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

# Somewhere later in your code, you can use it!
if honour_roll:
    print('Well done')

