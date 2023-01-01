'''
Escape Sequences
This is all of the escape sequences Python supports. 
______________________________________________________________________
|   \\           Backslash (\)
|   \'           Single-quote (’)
|   \"           Double-quote (”)
|   \a           ASCII bell (BEL)
|   \b           ASCII backspace (BS)
|   \f           ASCII formfeed (FF)
|   \n           ASCII linefeed (LF)
|   \N{name}     Character named name in the Unicode database (Unicode only)
|   \r           Carriage Return (CR)
|   \t           Horizontal Tab (TAB)
|   \uxxxx       Character with 16-bit hex value xxxx
|   \Uxxxxxxxx   Character with 32-bit hex value xxxxxxxx
|   \v           ASCII vertical tab (VT)
|   \000         Character with octal value 000
|   \xhh         Character with hex value hh
______________________________________________________________________
'''


print("\n\n\nI am\t 6'2\" tall.")
print('I am 6\'2" tall.\n\n\n')

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a cat \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip|n|t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

'''
Escape  sequence is compromised when using f'' Fstrings
And it is comented on Pep 8 
So it is not recommended to use with fstrings
'''
