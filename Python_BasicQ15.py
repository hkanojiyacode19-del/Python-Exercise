'''
Write a Python program to get the volume of a sphere with radius six.

'''

r = int(input("enter the radius of sphere : "))

from math import pi

volume = 4/3* pi * r**3

print(volume)