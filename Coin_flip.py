import random
import time
Head = input("Enter the thing you want heads to be: ")
Tail = input("Enter the thing you want tails to be: ")
times = input("How many times do you want to flip a coin: ")
i = 0
x = 1
y = 0
z = 0

while not i == float(times):
	print("\nFlipping in progress...")
	item = random.randint(0, 1)
	if item in [1]:
		print("\n" +  str(x) + ". Heads")
		x = x+1
		y = y+1
	elif item in [0]:
		print("\n" + str(x) + ". Tails")
		x = x+1
		z = z+1
	i = i+1

print("\nHeads occured: " + str(y) + " times and tails occured " + str(z) + " times.")
if y > z:
	print("\nHeads > Tails")
	print(Head + " won")
else:
	print("\nTail > Heads")
	print(Tail + " won")
