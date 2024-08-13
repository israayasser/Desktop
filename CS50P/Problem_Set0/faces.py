def main():
    """
    Main function to prompt the user for a text input containing emoticons and print the converted text.
    
    Prompts the user to enter a string with emoticons and then calls the convert function
    to replace the emoticons with their Unicode equivalents. Prints the resulting string.
    """
    # Get the user's input containing emoticons.
    emoticon = input("Write something with emoticon: ")
    
    # Convert emoticons in the input string and print the result.
    print(convert(emoticon))


def convert(emoticon):
    """
    Convert emoticons in a string to their Unicode equivalents.
    
    Args:
        emoticon (str): The input string containing emoticons to be converted.
    
    Returns:
        str: The input string with emoticons replaced by Unicode characters.
    """
    # Replace ":)" with the Unicode smiley face emoji.
    emoticon = emoticon.replace(":)", "🙂")
    
    # Replace ":(" with the Unicode frowning face emoji.
    emoticon = emoticon.replace(":(", "🙁")
    
    # Return the modified string.
    return emoticon

# Call the main function to execute the program.
main()
