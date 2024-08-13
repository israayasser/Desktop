# Prompt the user to enter an expression consisting of two operands and an operator.
expression = input("Expression: ")

# Split the input string into three parts: operand1, operator, and operand2.
x, y, z = expression.split(" ")

# Convert the operands from strings to integers.
x = int(x)
z = int(z)

# Evaluate the expression based on the operator.
if y == "+":
    # If the operator is "+", perform addition and print the result as a float.
    print(float(x + z))
elif y == "-":
    # If the operator is "-", perform subtraction and print the result as a float.
    print(float(x - z))
elif y == "/" and z != 0:
    # If the operator is "/" and the divisor is not zero, perform division and print the result as a float.
    print(float(x / z))
else:
    # For all other operators or if the divisor is zero, perform multiplication and print the result as a float.
    # Note: Division by zero is handled implicitly by this else block.
    print(float(x * z))