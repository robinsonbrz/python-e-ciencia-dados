'''
Ex 13 Parameters, Unpacking, Variables

'''

from sys import argv
# read the WYSS section for how to run this

# argv This LIST holds the arguments you pass to your Python script when you run
# the first agument is script name

# script, first, second, third = argv
list1 = []

# the following lin e unpacks argv in a list
print('Argv type', type(argv))

list1 = argv

for arg in list1:
    print(arg)


# print('The script is called', script)
# print('Your first variable is', first)
# print('Second variable or parameter', second)
# print('Third variable from parameter', third)

