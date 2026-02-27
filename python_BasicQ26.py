'''
Write a Python program to create a histogram from a given list of integers.


'''

def histogram(item):
        for i in item:
                output = ''
                times = i

                while times >0:
                        output += '*'
                        times = times -1 
                print(output)

histogram([14,22,12,7,3])

