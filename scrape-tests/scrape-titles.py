'''
This is the first program made with the help of chat gpt

'''


import requests
from bs4 import BeautifulSoup

def create_files(file_name_list):
    '''
    Receives a list of string as parameter to create files
    This code will create a Python file for each string in the strings list, 
    naming the file with the string followed by the .py extension. 
    It will then write the specified content to each file.
    '''

    strings = file_name_list

    for s in strings:
        # Open a file for writing and name it with the string
        with open(s + '.py', 'w') as f:
            # Write some content to the file
            f.write("'''\n" + s + "\n'''" )


def scrape_page():
    '''
    Scrape a page and returns all li elements texts as a list of strings
    '''
    url = 'https://learnpythonthehardway.org/python3/'

    # Fetch the webpage
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all elements with the class "simple"
    simple_elements = soup.find_all(class_='simple')

    # Find all the `li` elements within the elements with the class "simple"
    li_elements = []
    for element in simple_elements:
        li_elements.extend(element.find_all('li'))

    # Extract the text from each element and store it in a list


    li_texts = [li.text for li in li_elements if 'Exercise' in li.text]
    li_texts_final = []
    for text in li_texts:
        li_texts_final.append(text.replace('Exercise ', 'ex').replace(' ','-')
        .replace(':','').replace(',', '').replace('?','').lower())
    return li_texts_final

def create_file_store_name_files(list_file_names):
    '''
    Convert list to
    '''
    strings = list_file_names

    # Open a file for writing
    with open('strings.txt', 'w') as f:
        # Write each string to the file, followed by a newline character
        for s in strings:
            f.write(s + '\n')

li_texts = scrape_page()
create_file_store_name_files(li_texts)
create_files(li_texts)



