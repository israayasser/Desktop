# Get the user input and strip any extra spaces, then convert to lowercase
# This program greets the user and provides a response based on the greeting input.

# Prompt the user for a greeting and clean up the input
bank = input("Greeting: ").strip().lower()

# Check if the input contains "hello"
if "hello" in bank:
    print("$0")  # If "hello" is present, output $0
elif bank.startswith('h'):
    print("$20")  # If the input starts with 'h' but is not "hello", output $20
else:
    print("$100")  # For all other inputs, output $100