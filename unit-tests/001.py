'''Exercise 0
Print the Python version to the console. Use the built-in sys module.
Expected result:
3.8.10
'''

import sys
print(sys.version[:6])
print(sys.version.split("]")[0])