def main():
    """
    Main function to prompt the user for a file name and print its media type.
    
    Prompts the user to input a file name, converts it to lowercase, and
    then calls the media_type function to determine and print the file's media type.
    """
    # Get the file name from the user, convert it to lowercase, and strip any extra spaces.
    file = input("File name: ").strip().lower()
    
    # Determine and print the media type based on the file extension.
    print(media_type(file))

def media_type(file):
    """
    Determine the media type based on the file extension.
    
    Args:
        file (str): The file name including its extension.
    
    Returns:
        str: The media type corresponding to the file extension.
    """
    # Check the file extension and return the appropriate media type.
    if file.endswith(".gif"):
        return "image/gif"
    elif file.endswith(".jpg"):
        return "image/jpeg"
    elif file.endswith(".jpeg"):
        return "image/jpeg"
    elif file.endswith(".png"):
        return "image/png"
    elif file.endswith(".pdf"):
        return "application/pdf"
    elif file.endswith(".txt"):
        return "text/plain"
    elif file.endswith(".zip"):
        return "application/zip"
    else:
        # Return a default media type for unknown file extensions.
        return "application/octet-stream"

# Call the main function to execute the program.
main()
