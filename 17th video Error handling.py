# This code won't run at all! It' a SYNTAX ERROR
# x = 42
# y = 206
# if x == y
#     print('Success!')
    

# This code will fail when run! It' sa RUNTIME ERROR
# x = 42
# y = 0
# print(x/y)

# try: 
#     print(x / y)
# except ZeroDivisionError as e:
#     # Optionally, log e somewhere
#     print('Sorry something went wrong')
# except:
#     print('Something wen really went wrong')
# finally:
#     print('This always runs on success or failure')

# ___________________________________________

# This code won't run at all! It' a LOGIC ERROR

# x = 206
# y = 42
# if x < y:           # wrong sign
#     print(str(x) + ' is greater than ' + str(y))



# This code WILL RUN!!!!

# x = 206
# y = 42
# if x > y:
#     print(str(x) + ' is greater than ' + str(y))

q = 42
t = 0

print()
try:
    print(q / t)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
else:
    print('Something else went wrong')
finally:
    print('This is our cleanup code')
print()




