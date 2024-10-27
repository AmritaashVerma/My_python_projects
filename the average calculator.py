print("Hello There! I Welcome you to the average calculator.\nThis calculator can calculate the average of up to 10 numbers.\nThe minimum values needed for the calculator to work is 3.\nAfter 3 values are satisfied then you will be asked to enter values up to 10.\nEnter the number of values you want too enter and put a 0 in the values you don't want to enter.\nThese were all the instructions for the using of the calculator. Now let us find out some averages!")
unit_operation = input("What is the unit of the values you are giving? ")
first_average_value = input("Enter the first value: ")
second_average_value = input("Enter the second value: ")
third_average_value = input("Enter the third value: ")
fourth_average_value = input("Enter the fourth value: ")
fifth_average_value = input("Enter the fifth value: ")
sixth_average_value = input("Enter the sixth value: ")
seventh_average_value = input("Enter the seventh value: ")
eighth_average_value = input("Enter the eighth value: ")
ninth_average_value = input("Enter the ninth value: ")
tenth_average_value = input("Enter the tenth value: ")
if fourth_average_value in['0']:
    answer_one = (int(first_average_value) + int(second_average_value) + int(third_average_value)) / 3
    print("The average value of " + first_average_value + ", " + second_average_value + " and " + third_average_value + " is " + str(answer_one) + " " + unit_operation + ".")
if fifth_average_value in['0']:
    answer_two = (int(first_average_value) + int(second_average_value) + int(third_average_value) + int(fourth_average_value)) / 4
    print("The average value of " + first_average_value + ", " + second_average_value + ", " + third_average_value + " and " + fourth_average_value + " is " + str(answer_two) + " " + unit_operation + ".")
    if sixth_average_value in['0']:
        answer_three = (int(first_average_value) + int(second_average_value) + int(third_average_value) + int(fourth_average_value) + int(fifth_average_value)) / 5
        print("The average value of " + first_average_value + ", " + second_average_value + ", " + third_average_value + ", " + fourth_average_value + " and " + fifth_average_value + " is " + str(answer_three) + " " + unit_operation + ".")
        if seventh_average_value in['0']:
            answer_four = (int(first_average_value) + int(second_average_value) + int(third_average_value) + int(fourth_average_value) + int(fifth_average_value) + int(sixth_average_value)) / 6
            print("The average value of " + first_average_value + ", " + second_average_value + ", " + third_average_value + ", " + fourth_average_value + ", " + fifth_average_value + " and " + sixth_average_value + " is " + str(answer_four) + " " + unit_operation + ".")
            if eighth_average_value in['0']:
                answer_five = (int(first_average_value) + int(second_average_value) + int(third_average_value) + int(fourth_average_value) + int(fifth_average_value) + int(sixth_average_value) + int(seventh_average_value)) / 7
                print("The average value of " + first_average_value + ", " + second_average_value + ", " + third_average_value + ", " + fourth_average_value + ", " + fifth_average_value + ", " + sixth_average_value + " and " + seventh_average_value + " is " + str(answer_five) + " " + unit_operation + ".")
                if ninth_average_value in['0']:
                    answer_six = (int(first_average_value) + int(second_average_value) + int(third_average_value) + int(fourth_average_value) + int(fifth_average_value) + int(sixth_average_value) + int(seventh_average_value) + int(eighth_average_value)) / 8
                    print("The average value of " + first_average_value + ", " + second_average_value + ", " + third_average_value + ", " + fourth_average_value + ", " + fifth_average_value + ", " + sixth_average_value + ", " + seventh_average_value + " and " + eighth_average_value + " is " + str(answer_six) + " " + unit_operation + ".")
                    if tenth_average_value in['0']:
                        answer_seven = (int(first_average_value) + int(second_average_value) + int(third_average_value) + int(fourth_average_value) + int(fifth_average_value) + int(sixth_average_value) + int(seventh_average_value) + int(eighth_average_value) + int(ninth_average_value)) / 9
                        print("The average value of " + first_average_value + ", " + second_average_value + ", " + third_average_value + ", " + fourth_average_value + ", " + fifth_average_value + ", " + sixth_average_value + ", " + seventh_average_value + ", " + eighth_average_value + " and " + ninth_average_value + " is " + str(answer_seven) + " " + unit_operation + ".")
                    else:
                        answer_eight = (int(first_average_value) + int(second_average_value) + int(third_average_value) + int(fourth_average_value) + int(fifth_average_value) + int(sixth_average_value) + int(seventh_average_value) + int(eighth_average_value) + int(ninth_average_value) + int(tenth_average_value)) / 10
                        print("The average value of " + first_average_value + ", " + second_average_value + ", " + third_average_value + ", " + fourth_average_value + ", " + fifth_average_value + ", " + sixth_average_value + ", " + seventh_average_value + ", " + eighth_average_value + ", " + ninth_average_value + " and " + tenth_average_value + " is " + str(answer_eight) + " " + unit_operation + ".")


