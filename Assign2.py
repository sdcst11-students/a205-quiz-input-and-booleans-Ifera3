"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math

x = float(input("Enter a number: "))
y = float(input("Enter anouther number: "))

_isHypoth = bool(input("Is one number the hypothenuse? (enter Ture or False): "))

if _isHypoth:
    hyp = math.sqrt((max(x, y) ** 2) - (min(x, y) ** 2))
else:
    hyp = math.sqrt((x ** 2) + (y ** 2))
print(f"The hypothenuse is {round(hyp, 1)}")