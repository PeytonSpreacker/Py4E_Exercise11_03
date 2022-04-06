# imports regular expression library
import re

# starting sum value
sum = 0

# open the appropriate file from a user input
user_command = input('Select a file: ')
if len(user_command)<1:
    handle = open('regex_sum_1501839.txt')

# extract number strings from the file and add them
for line in handle:
    line.rstrip()
    num = re.findall('([0-9]+)', line)
    for i in num:
        inum = int(i)
        sum = sum + inum
print(sum)