def calculate(first, operator, second):
	if operator == "+":
		return first + second
	if operator == "-":
		return first - second
	if operator == "*":
		return first * second
	if operator == "/":
		if second == 0:
			raise ZeroDivisionError
		return first / second
	raise ValueError("Invalid operator")


while True:
	operator = input("Enter an operation (+, -, *, /) or q to quit: ").strip().lower()
	if operator in ("q", "quit"):
		print("Goodbye!")
		break

	if operator not in ("+", "-", "*", "/"):
		print("Invalid operator.")
		continue

	try:
		first = float(input("Enter the first number: "))
		second = float(input("Enter the second number: "))
		print(f"Result: {calculate(first, operator, second)}")
	except ValueError as error:
		if str(error) == "Invalid operator":
			print("Invalid operator.")
		else:
			print("Invalid number.")
	except ZeroDivisionError:
		print("Cannot divide by zero.")
