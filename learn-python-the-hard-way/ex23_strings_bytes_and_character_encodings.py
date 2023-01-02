'''
ex23-strings-bytes-and-character-encodings
Strings, Bytes, and Character Encodings

To do this exercise you’ll need to download a text file 
https://learnpythonthehardway.org/python3/languages.txt

1. How modern computers store human languages for display and processing and how Python 3 calls
this strings.
2. How you must ”encode” and ”decode” Python’s strings into a type called bytes.
3. How to handle errors in your string and byte handling.
4. How to read code and find out what it means even if you’ve never seen it before


'''

import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    '''
    recursive functions that reads line by line

    '''
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    '''
    function receives a line 
    and encodes and decode it into a string -> 
    cooked_string = Human readable lang encoded
    raw_bytes = Python numerical bytes, or the ”raw” bytes
    for printing to the screen

    if you have raw bytes, then you must use .decode() to get the string

    mnemonic ”DBES” which stands for ”Decode Bytes Encode Strings”

    '''

    # removes leading / trailing whitespace such as spaces, tabs, and newlines
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, '<===>', cooked_string)


# first line
languages = open('languages.txt', encoding=input_encoding)

main(languages, input_encoding, error)

    '''
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)