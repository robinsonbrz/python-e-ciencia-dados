'''
ex39-dictionaries-oh-lovely-dictionaries
'''

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {'CA': 'San Francisco',
          'MI': 'Detroit',
          'FL': 'Jacksonville'}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']]) # Cascade Detroit
print("Florida has: ", cities[states['Florida']])

print("\n\n every state abbreviation")
print('-' * 10)
for state, abbrev in states.items():
    print(f"{state} is abbreviated {abbrev}")

print("\n\n  print every city in state")
print('-' * 10)
for abbrev, city in cities.items():
    print(f"{abbrev} has the city {city}")

print("\n\n  now do both at the same time")
print('-' * 10)
for state, abbrev in states.items():
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default values
city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}")

print(states['Oregon'])

print(states.get('Oregano', 'Não existe'))

print("\nKeys")
print('-' * 10)
for keys in cities.keys():
    print(f"{ keys } ")

print("\nValues")
print('-' * 10)
for values in cities.values():
    print(f'{values}')

# Dictionaries can be show items(shows items and values)  , values, keys






### Error when trying to access a key that doesnt exist
### Thats why it's safer to use get
### because it allows you to use default value if the key doesnt exist
print(states['Oregano'])
