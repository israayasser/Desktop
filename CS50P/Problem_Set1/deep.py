# Prompt the user for the answer to the Great Question of Life, the Universe, and Everything.
deep = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").strip().lower()

# Check if the input matches the expected answers.
# Convert input to lowercase and remove any leading/trailing whitespace for comparison.
if deep == "42" or deep == "forty two" or deep == "forty-two":
    # If the input is one of the acceptable answers, print "Yes".
    print("Yes")
else:
    # If the input is not one of the acceptable answers, print "No".
    print("No")