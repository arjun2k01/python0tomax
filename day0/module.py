# import pyjokes
# joke=pyjokes.get_joke()
# print(joke)

# python can be used as a calculator
# repl is read-evaluate-print loop
# to run the code in the repl, type the code and press enter
# multiline comments can """ or ''' be used for multi-line comments"
'''
practise set 1:
write a program to print twinkle twinkle little star poem in python
Use a repl and print the table of 5 using it
Install an external module and use it to perform an operation of your interest.
Write a python program to print the contents of a directory using the os module.
Search online for the function which does that.
Label the program written in problem 4 with comments.
'''

# write a program to print twinkle twinkle little star poem in python
# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

# ''' you can also use triple quotes for multi-line strings

# Use a repl and print the table of 5 using it
# done in terminal

# Install an external module and use it to perform an operation of your interest.

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("PMGC is coming babyyyyyyy")
# engine.runAndWait()

# Write a python program to print the contents of a directory using the os module.

import os

# Specify the directory you want to list
directory = "/"

# List all files and folders in the specified directory
try:
    contents = os.listdir(directory)
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{directory}' does not exist.")
except PermissionError:
    print(f"Permission denied for accessing the directory '{directory}'.")

