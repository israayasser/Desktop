def main():
    """
    Main function to determine and print the meal time based on user input.
    
    The function prompts the user to input the current time in "HH:MM" format,
    converts the time to a floating-point hour value, and then checks if the
    time falls within predefined ranges for breakfast, lunch, or dinner. 
    It prints the corresponding meal time if it matches one of the ranges.
    """
    # Prompt the user to input the current time.
    time_input = input("What time is it? ").strip()

    # Convert the input time to a floating-point hour value.
    hour = convert(time_input)
    
    # Determine and print the meal time based on the hour value.
    if 7.0 <= hour <= 8.0:
        print("breakfast time")
    elif 12.0 <= hour <= 13.0:
        print("lunch time")
    elif 18.0 <= hour <= 20.0:
        print("dinner time")

def convert(time):
    """
    Convert a time string in "HH:MM" format to a floating-point hour value.

    Args:
        time (str): The time string in "HH:MM" format.
    
    Returns:
        float: The time converted to a floating-point hour value.
    
    Raises:
        ValueError: If the input time format is incorrect or the time is out of range.
    """
    # Split the time string into hours and minutes.
    hours, minutes = time.split(':')
    
    # Convert hours and minutes from strings to integers.
    hours = int(hours)
    minutes = int(minutes)

    # Validate that hours and minutes are within the correct range.
    if 0 <= hours < 24 and 0 <= minutes < 60:
        # Return the time as a floating-point value representing the hour.
        return hours + minutes / 60.0
    else:
        # Raise an error if the time values are out of range.
        raise ValueError("Invalid time format or out of range")

if __name__ == "__main__":
    # Execute the main function if this script is run as the main module.
    main()