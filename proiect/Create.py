import os.path

import os


def create(abc_latest, files):

    # Read the binary latest_file
    with open(abc_latest, 'rb') as compared_file:
        latest_file = compared_file.read()

    # Extract the name of the file
    diff_file_name = os.path.splitext(abc_latest)[0] + ".diff"

    # Create a new file with the extension .diff
    with open(diff_file_name, 'ab') as diff_file:

        # Read the binary files
        for file in files:
            with open(file, 'rb') as file_to_compare:
                current_file = file_to_compare.read()

                # Write the name of the file
                diff_file.write(str(os.path.splitext(file)[0] + os.path.splitext(file)[1]).encode('utf-8'))
                diff_file.write(b'\n')

                # Find and write the diff:

                # for change command

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
                end_of_file = "end of file: " + str(os.path.splitext(file)[0] + os.path.splitext(file)[1]) + "\n\n\n"
                diff_file.write(end_of_file.encode('utf-8'))

