print("Hello there this calculator converts temperature from\n1. Celcuis to Fahrenheit(C to F)\n2. Fahrenheit to Celcius(F to C)\n3. Celcius to Kelvin(C to K)\n4. Fahrenheit to Kelvin(F to K)\n5. Kelvin to Celcius(K to C)\n6. Kelvin to Fahrenheit(K to F)")
x, y = input("What would you like to convert?: ").split(" to ")

def main():
	if x in ['C', 'c'] and y in ['F', 'f']:
		Celcius = float(input("Celcius: "))
		Fahrenheit = round(float((Celcius * 1.8) + 32), 2)
		print(Celcius, " degree celcius is equal to ", Fahrenheit, " degree fahrenheit.")
	if x in ['F', 'f'] and y in ['C', 'c']:
		Fahrenheit = float(input("Fahrenheit: "))
		Celcius = round(float((Fahrenheit - 32) * 0.5556), 2)
		print(Fahrenheit, " degree fahrenheit is equal to ", Celcius, " degree celcius")
	if x in ['C', 'c'] and y in ['K', 'k']:
		Celcius = float(input("Celcius: "))
		Kelvin = float(Celcius + 273.15)
		print(Celcius, " degree celcius is equal to ", Kelvin, " degree kelvin.")
	if x in ['F', 'f'] and y in ['K', 'k']:
		Fahrenheit = float(input("Fahrenheit: "))
		Celcius = round(float((Fahrenheit - 32) * 0.5556), 2)
		Kelvin = float(Celcius + 273.15)
		print(Fahrenheit, " degree fahrenheit is equal to ", Kelvin, " degree kelvin")
	if x in ['K', 'k'] and y in ['C', 'c']:
		Kelvin = float(input("Kelvin: "))
		Celcius = round(float(Kelvin - 273.15), 2)
		print(Kelvin, " degree kelvin is equal to ", Celcius, " degree celcius.")
	if x in ['K', 'k'] and y in ['F', 'f']:
		Kelvin = float(input("Kelvin: "))
		Celcius = float(Kelvin - 273.15)
		Fahrenheit = round(float((Celcius * 1.8) + 32), 2)
		print(Kelvin, " degree kelvin is equal to ", Fahrenheit," degree fahrenheit")

main()