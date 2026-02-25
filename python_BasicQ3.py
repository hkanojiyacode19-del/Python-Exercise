'''
write an program to display the current data and time.
Current date and time :
2014-07-05 14:34:14

'''
import datetime # module is used to work with data and time

now = datetime.datetime.now()# get the current date and time
print(now)

print("current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))# using strftime method to format the datetime style