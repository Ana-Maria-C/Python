import os


def update(current_version, diff_file):
    """
    This function updates the current version of the file to the latest version of the file using the diff file
    : param current_version: the current version of the file (second parameter of the command line)
    : param diff_file: the diff file (third parameter of the command line)
    : return: None (just update the current version of the file by creating a new file with the extension .latest)
    """
    # Read the binary current_version
    try:
        with open(current_version, 'rb') as file:
            current_file = file.read()

        # Extract the name of the file
        output_name = os.path.splitext(current_version)[0] + ".latest"

        # open the diff_file and treat the exceptions
        try:
            """
            Open the diff file and search for the name of the current version of the file
            """
            with open(diff_file, 'rb') as file:
                found = False
                diff_line = file.readline()
                while diff_line:
                    if str(os.path.splitext(current_version)[0] + os.path.splitext(current_version)[1]) in diff_line.decode('utf-8'):
                        # print(diff_line.decode('utf-8'))
                        found = True
                        break
                    diff_line = file.readline()

                if found:
                    """
                    If the name of the current version of the file is found in the diff file, then search for the 
                    changes
                    """
                    end_of_file = "end of file: " + str(
                        os.path.splitext(current_version)[0] + os.path.splitext(current_version)[1]) + "\n"
                    diff_line = file.readline().decode('utf-8')
                    if diff_line == "change\n":
                        change_dict = {}
                        diff_line = file.readline().decode('utf-8')
                        while diff_line != end_of_file and diff_line != "insert\n" and diff_line != "delete from\n" and diff_line:
                            if ':' in diff_line:
                                key, value = diff_line.split(':')
                                change_dict[int(key)] = value
                            diff_line = file.readline().decode('utf-8')
                        # print(change_dict)

                        """
                        Apply the changes to the current version of the file by creating a new file with the extension 
                        .latest
                        """
                        # Apply the changes
                        try:
                            with open(output_name, 'wb') as output_file:
                                for i in range(len(current_file)):
                                    if i in change_dict:
                                        if change_dict[i] == '\n':
                                            output_file.write(change_dict[i].encode('utf-8'))
                                        else:
                                            output_file.write(change_dict[i].strip('\n').encode('utf-8'))
                                    else:
                                        output_file.write(bytes([current_file[i]]))

                        except IOError:
                            print(f"Error writing the file: {output_name}!")

                        """
                        After applying the changes, search for the insert/delete data
                        """
                        if diff_line == "insert\n":
                            diff_line = file.readline().decode('utf-8')
                            try:
                                with open(output_name, 'ab') as output_file:
                                    while diff_line != end_of_file and diff_line != "delete from\n" and diff_line:
                                        output_file.write(diff_line.encode('utf-8'))
                                        diff_line = file.readline().decode('utf-8')

                            except IOError:
                                print(f"Error writing the file: {output_name}!")

                        if diff_line == "delete from\n":
                            diff_line = file.readline().decode('utf-8')
                            try:
                                with open(output_name, 'ab') as output_file:
                                    while diff_line != end_of_file and diff_line:
                                        index_max = int(diff_line)
                                        # fix the max position
                                        output_file.seek(index_max)
                                        # eliminate the rest of the file
                                        output_file.truncate()
                                        break

                            except IOError:
                                print(f"Error writing the file: {output_name}!")
                else:
                    print(f"File: {current_version} not in the diff file: {diff_file}!")

        except FileNotFoundError:
            print(f"File: {diff_file} not found!")
        except IOError:
            print(f"Error reading the file: {diff_file}!")

    except FileNotFoundError:
        print(f"File: {current_version} not found!")
    except IOError:
        print(f"Error reading the file: {current_version}!")
