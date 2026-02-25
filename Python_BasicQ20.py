'''
Write a Python program that returns a string that is n (non-negative integer) copies of a given string.


'''

def copies (st,n):
    result = ""
    for i in range(n) :
        result = result+st
    return result

print(copies("Harsh",5)) 

