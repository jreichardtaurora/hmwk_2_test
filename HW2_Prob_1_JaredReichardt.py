'''
Created on Sep 13, 2019

@author: jared r
CSC1700 section AM
The purpose of this problem was to write a calculator that calculates 
the user's total shipping cost. It handles negative inputs properly, and prompts the user
for their package weight, and what type of shipping they used.
'''

def main():
    print("Starting Fast Freight Shipping Company Shipping Calculator")
    weight = float(input("What was your total package weight (in pounds)? "))
    while weight <= 0:
        weight = float(input("Error, please make sure your weight is a positive number: "))
    ship = input("Did you use Expedited (E) or Regular (R) shipping? ")
    if ship == 'E':
        shipping = "Expedited"
    elif ship == 'R':
        shipping = "Regular"
    
    if ship == 'E':
        if weight <= 2:
            rate = 1.5
        elif weight <= 6:
            rate = 3.0
        elif weight < 10:
            rate = 4.0
        else:
            rate = 4.75
    elif ship == 'R':
        if weight <= 2:
            rate = 1.0
        elif weight <= 6:
            rate = 2.0
        elif weight <= 10:
            rate = 3.0
        else:
            rate = 3.5
    
    total = rate * weight
    print(f"Your total package weight was {weight} pounds.")
    print(f"Your Selected Shipping was {shipping}.")
    print("Your total shipping cost will be $" + format(total, '.2f'))
    
main()    
        