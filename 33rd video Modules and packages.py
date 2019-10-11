#this file won't work, because imports are wrong

# import module as namespace
import helpes
helpers.display('Not a warning')

# import all into current namespace
from helpers import *
display('Not a warning')

# import specific items into current namespace
from helpers import display
display('Not a warning')


def display(message, is_warning=False):
    if is_warning:
        print('Warning!!')
    print(message)