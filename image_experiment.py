#x = 9
#y = 0.3
#
#if isinstance(x, float) or isinstance(y, float):
#	print("One of the values is float")
#else:
#	print("fail")

#list_ = [1, 2, 3]
#values = len(list_)
#total = 0
#
#for ele in range(0, values):
#	total = total + list_[ele]
#
#print(total)

list_ = []
x = input("num: ")
for i in range(1, int(x)+1):
	if x % i == 0:
		list_.append(i)

print("Factors of " + str(x) + " are ", list_)