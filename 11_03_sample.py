# imports regular expression library
import re

# open the appropriate file from a user input
user_command = input('Select a file: ')
if len(user_command)<1:
    handle = open('regex_sum_1501839.txt')

