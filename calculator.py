while True:
	number1 = input("Enter your first number (between 1 and 1): ")
	number2 = input("Enter your second number (between 1 and 1): ")
	operation = input("Enter the operation (*, +, -, /): ")
	if operation == "+":
		if number1 == "1" and number2 == "1":
			print("1 + 1 = 2")
	elif operation == "-":
		if number1 == "1" and number2 == "1":
			print("1 - 1 = 0")
	elif operation == "*":
		if number1 == "1" and number2 == "1":
			print("1 * 1 = 1")
	elif operation == "/":
		if number1 == "1" and number2 == "1":
			print("1 / 1 = 1.0")
	else:
		print("invalid operation")
