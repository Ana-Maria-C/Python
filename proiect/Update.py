import sys
import os
import difflib


def update(current_version, diff_file):
    # Read the binary current_version
    with open(current_version, 'rb') as file:
        current_file = file.read()

    # Extract the name of the file
    output_name = os.path.splitext(current_version)[0] + ".latest"

    # open the diff_file

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
            end_of_file = "end of file: " + str(os.path.splitext(current_version)[0] + os.path.splitext(current_version)[1]) + "\n"
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

                # Apply the changes
                with open(output_name, 'wb') as output_file:
                    for i in range(len(current_file)):
                        if i in change_dict:
                            if change_dict[i] == '\n':
                                output_file.write(change_dict[i].encode('utf-8'))
                            else:
                                output_file.write(change_dict[i].strip('\n').encode('utf-8'))
                        else:
                            output_file.write(bytes([current_file[i]]))

                if diff_line == "insert\n":
                    diff_line = file.readline().decode('utf-8')
                    with open(output_name, 'ab') as output_file:
                        while diff_line != end_of_file and diff_line != "delete from\n" and diff_line:
                            output_file.write(diff_line.encode('utf-8'))
                            diff_line = file.readline().decode('utf-8')

                if diff_line == "delete from\n":
                    diff_line = file.readline().decode('utf-8')
                    with open(output_name, 'ab') as output_file:
                        while diff_line != end_of_file and diff_line:
                            index_max = int(diff_line)
                            # fix the max position
                            output_file.seek(index_max)
                            # eliminate the rest of the file
                            output_file.truncate()
                            break
