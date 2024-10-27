from timeit import default_timer as timer

num = input("Enter your main number: ")
multi = input("Enter the number of zeros you want to add to the main number: ")
start = timer()
list1 = [*str(num)]
s = "0"

try:
	for i in range(0, int(multi)):
		list1.append(s)
	ans = (''.join(list1))
	print(ans)
	length = len(ans)
	print('{:,}'.format(length) + "! Is the amount of characters the calculation reached")
except KeyboardInterrupt:
	ans = (''.join(list1))
	length = len(ans)
	print('{:,}'.format(length) + "! Is the amount characters the calculation reached")
end = timer()
print(start-end)