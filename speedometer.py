print("Hello there, you can calculate the speed by giving the distance and time taken to cover that distance "
      "with this calculator")
distance = input("Enter the distance: ")
time = input("Enter the time taken to cover the distance: ")
unit = input("Enter the unit of measurement(like kph, mph, m/s etc.)")
answer = int(distance) / int(time)
print("The speed is " + str(answer) + " " + unit)

