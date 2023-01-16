'''
https://docs.python.org/3/library/shutil.html
Script que compacta arquivos de uma pasta em um único arquivo zip
'''


import shutil

# The zip files you want to add to the archive
files_to_archive = "./zips"

# The name of the archive file you want to create
archive_name = 'archive'

# The format of the archive file, in this case it's zip
archive_format = 'zip'

# Cria um arquivo com todos os arquivos do diretorio ./zips
shutil.make_archive(archive_name, archive_format, files_to_archive)

# Delete the folder and its contents
shutil.rmtree(files_to_archive)