import time
def fast():
    unit_operation = input("What unit would you like to give? ")
    x = [float(x) for x in input("Enter all your values: ").split(", ")]
    y = int(len(x))
    answer = int((sum(x)) / y)
    print("The average of", x, "is", str(answer), unit_operation)
print("Hello There! Welcome to the average calculator.")
time.sleep(3)
response = input("Do you want to skip the tutorial(Y or n): ")
if response in ['Y', 'y']:
    print("Great! Now let us find out some averages!")
    fast()
elif response in['n', 'N']:
    print("This calculator can calculate the average of infinite numbers.")
    time.sleep(3)
    print("just seperate the diffrent numbers with commas and don't seperate the thousands and so on places with commas")
    time.sleep(3)
    print("Now lets go and find some averages!")
    time.sleep(1)
    fast()
else: 
    print("Error 400: Bad response")

##the inefficient way
#def slow():
#    unit_operation = input("What is the unit of the values you are giving? ")
#    first_average_value = input("Enter the first value: ")
#    second_average_value = input("Enter the second value: ")
#    third_average_value = input("Enter the third value: ")
#    proceding_one = input("Would you like to continue to enter more number? ")
#    if proceding_one in['no', 'n']:
#        answer_one = (int(first_average_value) + int(second_average_value) + int(third_average_value)) / 3
#        print("The average of the three numbers you have entered till now is " + str(answer_one) + " " + unit_operation + ".")
#    else:
#        fourth_average_value = input("Enter the fourth value: ")
#        fifth_average_value = input("Enter the fifth value: ")
#        sixth_average_value = input("Enter the sixth value: ")
#        proceding_two = input("Would you like to enter more values? ")
#        if proceding_two in['no']:
#            answer_two = (int(first_average_value) + int(second_average_value) + int(third_average_value) + int(fourth_average_value) + int(fifth_average_value) + int(sixth_average_value)) / 6
#            print("The average of the six numbers you have entered till now is " + str(answer_two) + " " + unit_operation + ".")
#        else:
#            seventh_average_value = input("Enter the seventh value: ")
#            eight_average_value = input("Enter the eight value: ")
#            ninth_average_value = input("Enter the ninth value: ")
#            tenth_average_value = input("Enter the tenth value: ")
#            answer_three = (int(first_average_value) + int(second_average_value) + int(third_average_value) + int(fourth_average_value) + int(fifth_average_value) + int(sixth_average_value) + int(seventh_average_value) + int(eight_average_value) + int(ninth_average_value) + int(tenth_average_value)) / 10
#            print("The average of all the numbers you have entered is " + str(answer_three) + " " + unit_operation + ".")