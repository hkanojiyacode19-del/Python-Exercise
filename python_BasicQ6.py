'''
Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
'''
series_no = input("Enter you series of number : ")
num_list= series_no.replace(" ","").split(",") # never do [series_no.replace(" ","").split(",")] it create list under an list not an series of no of list
num_tuple = tuple(series_no.replace(" ","").split(","))# never do (series_no.replace(" ","").split(",")) it make only list inside the tupel you must declare
print(type(num_list))
print(num_list)
print(type(num_tuple))
print(num_tuple)

