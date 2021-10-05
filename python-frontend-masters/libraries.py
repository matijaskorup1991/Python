# from pprint import pprint
# from my_math_functions import add_numbers
import os
import sys
# print(add_numbers(2, 5))

# pprint({num: num * num for num in range(100)})

my_folder = os.getcwd()
print(my_folder)

# with os.scandir(my_folder) as folder:
#     for entry in folder:
#         print(entry.name)

# arguments = sys.argv
arguments = sys.argv[1:]
print(arguments)
print(f"we are running on a {sys.platform} machine")
