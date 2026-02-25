'''
Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days

'''
# MY SOLTION
# first_date = input("Enter the first date in Year-month-day format : ")
# Second_date = input("Enter the first date in Year-month-day format : ")

# f =first_date.split("-")
# s = Second_date.split("-")
# print(f)

# n=0

# for i in f:
#     print(int(f[n])-int(s[n]))
#     if (n==0):
#         print("year ",int(f[n])-int(s[n]))
#     elif(n==1):
#         print("month",int(f[n])-int(s[n]))
#     else:
#         print("Day",int(f[n])-int(s[n]))
#     n += 1

    #using Build in fucnion

from datetime import date

F_date = date(2025,2,5)
S_date = date(2024,5,5)

delta = S_date - F_date

print(delta)
    