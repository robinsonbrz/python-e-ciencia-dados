import os

def rename_files(directory, old_char, new_char):
    filenames = os.listdir(directory)
    for filename in filenames:
        new_filename = filename.replace(old_char, new_char)
        if old_char in filename:
            print(filename) 
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)
            print(old_path, new_path)
            os.rename(old_path, new_path)

# Exemplo de uso
directory = './om/'
old_char = '-'
new_char = '_'
rename_files(directory, old_char, new_char)