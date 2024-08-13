def main():
    """
    Calculate and print the tip amount based on meal cost and tip percentage.
    """
    # Convert input meal cost to a float.
    dollars = dollars_to_float(input("How much was the meal? "))
    
    # Convert input tip percentage to a float.
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculate the tip amount.
    tip = dollars * percent
    
    # Print the tip amount, formatted to 2 decimal places.
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    Convert a dollar amount string to a float.
    """
    return float(d.replace("$", ""))


def percent_to_float(p):
    """
    Convert a percentage string to a float.
    """
    return float(p.replace("%", "")) / 100

# Run the main function.
main()
