from math import *

response = input ("Which operation would you like to perform? Square root or cube root? Enter your response here: ")

if response in ["square root", " square root", "square"]:
    print ("you have chosen square root operation.")
    number = input ("What is the number you would like to square root? Enter the number here(only the number): ")
    converted_num = int(number)
    print ("The square root of " + number + " is")
    print (sqrt(converted_num))
    print ("Thank You for using this calculator")
else:
    print ("Oops there was a problem in registering your response! If you chose cube root it is in the following statements")

    if response in ["cube root", " cube root", "cube"]:
        print ("You have chosen the cube root operation")
        cube_num = input ("Enter the number that you would like to find the cube root of(only the number): ")
        converted_cube_num = int(cube_num)
        cr = converted_cube_num ** (1./3)
        print ("The cube root of " + cube_num + " is " + str(cr) + ".")
        print ("Thank you for using this calculator.")
    else:
        print ("oops there was a problem in getting your response.")


