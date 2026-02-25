'''
Write a Python program to calculate the difference between a given number and 17.
 If the number is greater than 17, return twice the absolute difference.
 
'''

num = int(input("Enter the number : "))
difference = 17 - num

if (num > 17):
    print("the Twise of the difference is : ",difference*2)
else:
    print("the difference is : ", difference)