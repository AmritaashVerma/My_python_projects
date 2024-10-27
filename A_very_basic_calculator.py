from decimal import *

print("Hello there this is a arithmetic calculator that can add/subtract/multiply/divide upto 3 digits")

operation = input("What would you like to perform?\n1. Add(+)\n2. Subtract(-)\n3. Multiply(*)\n4. Divde(/)\n5. Find remainder of two numbers(%)\nYour response: ")

if operation in ['+']:
	print("You have chosen addition")
	num1 = float(input("1st number: "))
	num2 = float(input("2nd number: "))
	num3 = float(input("3rd number: "))
	answer = num1 + num2 + num3
	res = input("Do you want to round off your answer to one decimal place(y or n)? ")
	if res in ['y', ' y', 'Y', ' Y']:
		print("Answer = " + str(round(answer, 1)))
	elif res in ['n', ' n', 'N', ' N']:
		print("Answer = "+ str(answer))
elif operation in ['-']:
	print("You have chosen subtraction")
	num1 = float(input("1st number: "))
	num2 = float(input("2nd number: "))
	num3 = float(input("3rd number: "))
	answer = num1 - num2 - num3
	print("Answer = "+ str(answer))
elif operation in ['*']:
	print("You have chosen multiplication")
	num1 = float(input("1st number: "))
	num2 = float(input("2nd number: "))
	num3 = float(input("3rd number: "))
	answer = num1 * num2 * num3
	print("Answer = " + str(answer))
elif operation in ['/']:
	print("You have chosen Division")
	y = input("Do you want to divide 3 numbers(3) or 2 numbers(2): ")
	if y in ['3']:
		num1 = float(input("1st number: "))
		num2 = float(input("2nd number: "))
		num3 = float(input("3rd number: "))
		answer = num1 / num2 / num3
		print("Answer = " + str(answer))
	elif y in ['2']:
		num1 = float(input("1st number: "))
		num2 = float(input("2nd number: "))
		answer = num1 / num2
		print("Answer = " + str(answer))
	else:
		print("Error 304: Bad response.")
elif operation in ['%']:
	print("You have chosen to find out the remainder of two numebers")
	num1 = float(input("1st number: "))
	num2 = float(input("2nd number: "))
	answer = num1 % num2
	print("Anser = " + str(answer))
else: 
	print("Error 304: Bad response.")