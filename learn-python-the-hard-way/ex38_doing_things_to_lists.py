'''
ex38-doing-things-to-lists
'''


ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There's {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
print("stuff", stuff)

print("' '.join(stuff)")
print(' '.join(stuff))  # what= cool!

print("'#'.join(stuff[3:5])")
print('#'.join(stuff[3:5]))  # super stellar!

'''
Saída a partir da linha 10
stuff ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana']
' '.join(stuff)
Apples Oranges Crows Telephone Light Sugar Boy Girl Banana
'#'.join(stuff[3:5])
Telephone#Light
'''
