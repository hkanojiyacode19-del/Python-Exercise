'''
Write a Python program that concatenates all elements in a list into a string and returns it.


'''
def merge(l):
    output = ''
    for i in l:
        output += str(i)
    return output        

    

print(merge([1,2,3,4,5,6,7,8,9]))