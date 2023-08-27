'''
Exercise 2
Assert the is_canada variable using the assert statement:



countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_canada = 'CAN' in countries


Expected action: Raising AssertionError.
'''

countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_canada = 'CAN' in countries

import unittest


class TestIsCanadaInListCountries(unittest.TestCase):

    def test_is_country_canada_in_list_countries(self):
        self.assertEqual(is_canada, True)
    
if __name__ == "__main__":
    unittest.main()


# Solução do Udemy
# assert is_canada, 'Country Canada not found'
