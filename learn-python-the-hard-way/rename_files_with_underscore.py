'''

ways to import 

import ex25_even_more_practice
from ex25_even_more_practice import *
'''


import os

def read_filenames(directory):
    # Get the filenames in the specified directory
    filenames = os.listdir(directory)
    return filenames

def replace_hyphens(strings):
    # Replace hyphens with underscores in each string
    modified_strings = [s.replace('-', '_') for s in strings]
    return modified_strings

def rename_files(filenames, modified_filenames):
    # Rename the files in the directory using the modified filenames
    for i in range(len(filenames)):
        os.rename(filenames[i], modified_filenames[i])

# Test the functions
directory = './'
filenames = read_filenames(directory)
modified_filenames = replace_hyphens(filenames)

rename_files(filenames, modified_filenames)