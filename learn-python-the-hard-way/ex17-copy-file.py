'''
We’ll write a Python script to copy one file to anothe
'''

    # from sys import argv
    # from os.path import exists

    # script, from_file, to_file = argv

    # print(f"\n\nEx17\nCopying from {from_file} to {to_file} ")

    # # it could be done in one line
    # in_file = open(from_file)
    # in_data = in_file.read()

    # print(f'The input file is {len(in_data)} bytes long')

    # print(f'Does the output file exist? {exists(to_file)}')
    # print('Ready, hit RETURN TO CONTINUE, CTRL-C to abort.')
    # input()

    # out_file = open(to_file, 'w' )
    # out_file.write(in_data)

    # print("Alright, all done.")

    # out_file.close()
    # in_file.close()


from os.path import exists
'''
Ex 17 variation


'''

#script, from_file, to_file = argv

from_file = input("\n\nDigite um arquivo que deseja copiar: \n > ")

to_file = input("Digite o nome arquivo de destino (cópia):  \n > ")


print(f"\n\nEx17\nCopying from {from_file} to {to_file} ")

# it could be done in one line
# in_data = open(from_file).read() 
# in_file = open(from_file); in_data = in_file.read()  # maneira cretina

in_file = open(from_file)
in_data = in_file.read()

print(f'The input file is {len(in_data)} bytes long')

print(f'Does the output file exist? {exists(to_file)}')
print('Ready, hit RETURN TO CONTINUE, CTRL-C to abort.')
input()

out_file = open(to_file, 'w' )
out_file.write(in_data)

print("Alright, all done.")

out_file.close()
in_file.close()