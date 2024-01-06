import sys
from Create import create
from Update import update


def main():
    """
    This is the main function of the program
    Use the command 'create' from Create.py to create a diff file (contains the differences between the current version
        and the previous versions)
    Use the command 'update' from Update.py to update a file (update the current version to the latest version using the
        diff file)
    : return: None
    """
    if len(sys.argv) < 3:
        print("Usage: python DiffUpdate.py current_version previous_version1 previous_version2 ...")
    else:
        command = sys.argv[1]
        current_version = sys.argv[2]
        if command == 'create':
            previous_versions = sys.argv[3:]
            create(current_version, previous_versions)
        else:
            previous_versions = sys.argv[3]
            update(current_version, previous_versions)


if __name__ == '__main__':
    main()
