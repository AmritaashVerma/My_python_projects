# accept the height of an individual in inches and convert it in feet and inches
import math

height = float(input("What is you height in just inches: "))
z = height
height = round(height) / 12
print("Your height is", height, "and", z-height, "inches.")