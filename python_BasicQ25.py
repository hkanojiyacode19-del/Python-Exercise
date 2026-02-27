'''
write a python program that checks weather a specified value is contained within a group of values.
test data

3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False

'''
def check_list(l,i):
    if i in l :
        print (True)
    else:
        print(False)


check_list([1,2,3,4,5,6,7,8,9],15)

