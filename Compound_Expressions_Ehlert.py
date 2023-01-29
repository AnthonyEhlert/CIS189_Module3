"""
Program: Compound_Expressions_Ehlert.py
Author: Tony Ehlert
Last date modified: 1/25/2023

The purpose of this program is to compare a variable between two constant values using compound expressions
The input is an integer
The output is the results of the different comparisons
"""
# import of Constants.py
from Constants import MAX, MIN

# creation of x & y variables
y = 5
x = 10

print("y > MAX, " + str((y > MAX)))
print("y < MIN, " + str((y < MIN)))
print("MIN < x < MAX, " + str((MIN < x < MAX)))
