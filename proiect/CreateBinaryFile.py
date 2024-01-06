import sys


def create_binary_file(file_path_content):
    """
    This function creates a binary file from a text file
    : param file_path_content: the path of the text file
    : return: None(just creates the binary file)
    """
    try:
        with open(file_path_content, 'r') as input_file:
            # Reading the text from the file
            text_content = input_file.read()

    except FileNotFoundError:
        print(f"File: {file_path_content} not found!")
    except IOError:
        print(f"Error reading the file: {file_path_content}!")

    # Creating the path of the binary file
    file_path = file_path_content[:-4] + "_binary.bin"

    try:
        with open(file_path, 'wb') as output_file:
            # Writing the text to the binary file
            output_file.write(text_content.encode('utf-8'))

    except FileNotFoundError:
        print(f"File: {file_path} not found!")
    except IOError:
        print(f"Error writing the file: {file_path}!")


def main():
    """
    This is the main function of the program
    : return: None
    """
    if len(sys.argv) < 2:
        print("Usage: python CreateBinaryFile.py file_path_content")
    else:
        file_path_content = sys.argv[1]
        create_binary_file(file_path_content)


if __name__ == '__main__':
    main()
