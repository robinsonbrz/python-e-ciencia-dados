'''
Now you will learn about reading from a file
This exercise involves writing two files. 


'''
from sys import argv

script, filename = argv

txt = open(filename)


print(f"Here's your filename: {filename}")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())



