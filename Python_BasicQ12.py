
'''
Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.

'''

import calendar 

Y = int(input("Input the Year : "))
m = int(input("input the month : "))

print(calendar.month(Y,m))