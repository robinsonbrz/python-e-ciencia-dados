'''
Reading and Writing Files

• open opens the file, parameter: w write, r read and a append to the file
        If you use w, all the previous content is lost, and the new content is writen
• close – Closes the file. Like File->Save.. in your editor.
• read – Reads the contents of the file. You can assign the result to a variable.
• readline – Reads just one line of a text file.
• truncate – Empties the file. Watch out if you care about the file.
• write('stuff') – Writes ”stuff” to the file.
• seek(0) – Move the read/write location to the beginning of the file
'''

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}. ")
print("If you don't want that, CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")


target = open(filename, 'w')

print("Truncating the file. Goodbye!")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("And finally, we close it.")
target.close()