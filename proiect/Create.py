import os


def create(abc_latest, files):

    """
    Create a new file with the extension .diff
    This file contains the differences between the latest version and the current version of the files
    : param abc_latest: the latest version of the file (second parameter of the command line)
    : param files: the current version of the files (starting from the third parameter of the command line)
    : return: None (just create the diff file)
    """
    # Read the binary latest_file
    try:
        with open(abc_latest, 'rb') as compared_file:
            latest_file = compared_file.read()

        # Extract the name of the output file
        diff_file_name = os.path.splitext(abc_latest)[0] + ".diff"

        # Create the output file with the extension .diff and treat the exceptions
        try:
            with open(diff_file_name, 'ab') as diff_file:

                """
                The structure of the diff file is:
                
                name of the file
                change
                index:character 
                insert
                characters      
                delete from
                index           
                end of file: name of the file
                """
                # Read the binary files and treat the exceptions
                for file in files:
                    try:
                        with open(file, 'rb') as file_to_compare:
                            current_file = file_to_compare.read()

                            # Write the name of the file
                            diff_file.write(str(os.path.splitext(file)[0] + os.path.splitext(file)[1]).encode('utf-8'))
                            diff_file.write(b'\n')

                            # Find and write the diff:

                            # for change command
                            """
                            The structure of the change command is:
                            change
                            index:character
                            
                            index is the index of the character that is different in the latest version of the file
                            character is the character from the latest version of the file
                            """
                            command = "change\n"
                            diff_file.write(command.encode('utf-8'))

                            max_index = min(len(current_file), len(latest_file))
                            for i in range(max_index):
                                if current_file[i] != latest_file[i]:
                                    diff_file.write(str(i).encode('utf-8'))
                                    separator = ':'
                                    diff_file.write(separator.encode('utf-8'))
                                    diff_file.write(bytes([latest_file[i]]))
                                    diff_file.write(b'\n')

                            # for insert/delete command
                            """
                            The structure of the delete command is:
                            delete from
                            index
                            
                            index is the index from where the characters are deleted in the latest version of the file
                            """

                            """
                            The structure of the insert command is:
                            insert
                            characters
                            
                            characters are the characters that are inserted in the latest version of the file
                            """

                            if len(current_file) > len(latest_file):
                                command = "delete from\n"
                                diff_file.write(command.encode('utf-8'))
                                diff_file.write(str(len(latest_file)).encode('utf-8'))
                                diff_file.write(b'\n')
                            elif len(current_file) < len(latest_file):
                                command = "insert\n"
                                diff_file.write(command.encode('utf-8'))
                                diff_file.write(latest_file[len(current_file):])
                                diff_file.write(b'\n')

                            # End of the current_file
                            """
                            The structure of the end of the file is:
                            end of file: name of the file
                            
                            I use this structure to know when I reached the end of the modifications for the current file
                            """
                            end_of_file = "end of file: " + str(os.path.splitext(file)[0] + os.path.splitext(file)[1]) + "\n\n\n"
                            diff_file.write(end_of_file.encode('utf-8'))

                    except FileNotFoundError:
                        print(f"File: {file} not found!")
                    except IOError:
                        print(f"Error reading the file: {file}!")

        except IOError:
            print(f"Error creating or writing the diff file: '{diff_file_name}!")

    except FileNotFoundError:
        print(f"File: {abc_latest} not found!")
    except IOError:
        print(f"Error reading the file: {abc_latest}!")
