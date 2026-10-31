# if else
import os

name = input(" What is your name?:")

age = input("Enter the age:")  # 20 '20'

if age.isnumeric():
    print("Invalid age")
    # terminate
    os._exit(0)
    # sys.exit()


if int(age) > 18:
    print(name + " is an adult")
else:
    print(name + " is a Child")

# lists, booleans, tuples, dictionary, loops


