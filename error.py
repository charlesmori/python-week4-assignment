def read_file_with_error_handling():
    filename = input("Please enter the filename: ")

    try:
        # Try opening and reading the file
        with open(filename, 'r') as file:
            content = file.read()
        print(f"File content:\n{content}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
read_file_with_error_handling()