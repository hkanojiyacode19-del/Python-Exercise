'''
Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
'''

file_name = input("input the filename: ")
f_extns = file_name.split(".")
#print the extension file, which is the last element in the "f_extns" list 
print("the Extension of the file is : " + repr(f_extns[-1])) # dought