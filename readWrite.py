def modify_file_content(input_filename, output_filename):
    try:
        # Read content from the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (for example, convert text to uppercase)
        modified_content = content.upper()  # Modify as needed

        # Write modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Content modified and written to {output_filename}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage:
modify_file_content('input.txt', 'modified_output.txt')