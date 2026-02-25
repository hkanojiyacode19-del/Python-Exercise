'''
Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
 Return the string unchanged if the given string already begins with "Is".

'''
def is_f (s):
# for more optimized solution use this  
# # Check if the length of the "text" is greater than or equal to 2 and if the first two characters of "text" are "Is"
# if len(text) >= 2 and text[:2] == "Is":
    if ("is" not in s ):
        print(s)
    else:
        print("is "+s) 

st = "Iam harsh kanojiya of Devops using python class"
st1 = "and it is very great class"

is_f(st1)