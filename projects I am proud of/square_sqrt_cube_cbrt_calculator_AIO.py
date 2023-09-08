from math import *
import math
import time

def main():
    thing_to_calculate = input("What operation would you like to carry out, square(press 1), cube(Press 2), a custom exponent(Press 3), square root(Press 4) or cube root(Press 5): ")
    if thing_to_calculate in ['3']: 
        print("You have chosen to give a custom exponent to a particualar number.")
        exponent = input("Input the exponent: ")
        number_expo = input("Input the number: ")
        try:
            answer_expo = math.pow(float(number_expo), float(exponent))
        except OverflowError:
            answer_expo = float('inf')
        print(number_expo + " to the power " + exponent + " equals to " + str(('{:,.2f}'.format(answer_expo))))
    if thing_to_calculate in ['1']:
        print ("You have chosen the operation to square a number")
        number_sqr = input ("What is the number you would like to square(please add no spaces in entering the number & don't seperate the number with commas): ")
        print ("The square of " + number_sqr + " is", end=" ")
        print('{:,.10f}'.format(math.pow(float(number_sqr), 2)))
        print("Thank you for using this calculator")
    if thing_to_calculate in ['2']:
        print ("You have chosen the operation to cube a number.")
        number_cube = input ("What is the number you would like to cube(please add no spaces in entering the number & don't seperate the number with commas)? ")
        print ("The cube of " + number_cube + " is", end=" ")
        print ('{:,.2f}'.format(math.pow(float(number_cube), 3)))
        print("Thank you for using this calculator")
    if thing_to_calculate in ['5']:
        print ("You have chosen the cube root operation")
        cube_num = input ("Enter the number that you would like to find the cube root of(only the number & add no spaces & don't seperate the number with commas): ")
        converted_cube_num = float(cube_num)
        cr = converted_cube_num ** (1./3)
        print ("The cube root of " + cube_num + " is", end=" ")
        print ('{:,.2f}'.format(cr))
        print ("Thank you for using this calculator.")
    if thing_to_calculate in ['4']:
        print ("you have chosen square root operation.")
        number = input ("What is the number you would like to find the square root of? Enter the number here(only the number & add no spaces & don't seperate the number with commas): ")
        converted_num = float(number)
        print ("The square root of " + number + " is", end=" ")
        print ('{:,.2f}'.format(sqrt(converted_num)))
        print ("Thank You for using this calculator")
    if not thing_to_calculate in ['1', '2', '3', '4', '5',]:
        print("You have chosen/typed an invalid operation!\nThank you for NOT using this calculator.")

print("Hello there and this is a collective square, square root and cube, cube root calculator!")
time.sleep(1) 
tutorial_prompt = input("Do you want to skip the beginners' tutorial?[y or n]")
if tutorial_prompt in ['n']:
    print("To use this calculator follow these steps:")
    time.sleep(3)
    print("Step 1: \nType in the operation you want to execute.")
    time.sleep(3)
    print("Step 2:\nType in the number you want to execute the operation on")
    time.sleep(3)
    print("Step 3:\nVoila! There you have it ur result.")
    time.sleep(3)
    print("So now let us get into some calculations!")
    main()
if tutorial_prompt in ['y']:
    print("looks like you are a smart person! So lets get directly into the calculation.")
    main()  
if not tutorial_prompt in ['n', 'y']:
    print("Error 404: Response invalid")
