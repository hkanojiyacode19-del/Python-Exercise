'''
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
'''
Radius = int(input("Enter the radius of the circle : "))
Area = Radius **2 * 3.14
print(f"area of the circle is {Area} Unit^2") 

# or another way for more accurate result is

from math import pi

Radius = int(input("Enter the radius of the circle : "))
Area = Radius **2 * pi
print(f"area of the circle is {Area} Unit^2") 