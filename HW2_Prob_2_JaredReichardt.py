'''
Created on Sep 16, 2019

@author: Jared R
CSC1700 section AM
This program will prompt the user for three integers.
It will then display the integers in a non-decreasing order.
'''

one = int(input("Please enter your first integer: "))
two = int(input("Please enter your second integer: "))
three = int(input("Please enter your third integer: "))

largest = one

middle = two

smallest = three

if two > largest:
    largest = two
elif three > largest:
    largest = three

if one < smallest:
    smallest = one
elif two < smallest:
    smallest = two

if one < largest:
    if one > smallest:
        middle = one

if two < largest:
    if two > smallest:
        middle = two

if three < largest:
    if three > smallest:
        middle = three

print("This is your three numbers in non-decreasing order")
print(str(smallest) + ' ' + str(middle) + ' ' + str(largest))
