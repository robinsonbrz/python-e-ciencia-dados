'''
Exercise 1
Assert the is_italy variable using the assert statement:

countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_italy = 'ITA' in countries

'''

countries = ['POL', 'ENG', 'GER', 'USA', 'ITA']
is_italy = 'ITA' in countries

# Enter your solution here
import unittest

class TestItaInCountriesList(unittest.TestCase):

    def test_ita_in_list(self):
        assert is_italy == True


if __name__ == "__main__":
    unittest.main()


# assert is_italy, 'Italy not found in the countries list.'